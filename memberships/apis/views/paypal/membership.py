from rest_framework.decorators import api_view, permission_classes
from memberships.models import Membership, UserMembership
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from datetime import timedelta
from django.utils import timezone
from memberships.tasks import send_notification_after_sub
from globals.paypal_utils import get_auth_token
import requests
import json


@api_view(["POST",])
@permission_classes([UserActive])
def initiate_subscription(request):
    data = request.data
    user = request.user

    if not data:
        return Response({
            "message": "No data to initiate the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("membership_name")
    months = data.get("months", 1)

    if not name:
        return Response({
            "message": "Please enter the membership name"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        membership = Membership.objects.get(name=name)
    except Membership.DoesNotExist:
        return Response({
            "message": "There's no membership with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    has_membership = UserMembership.objects.filter(subscriber=user).exists()

    if has_membership:
        return Response({
            "message": "Cannot initiate a subscription for already subscribed member"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        auth_token = get_auth_token()
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while initiating the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        data = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "items": [
                        {
                            "name": str(membership.name),
                            "quantity": str(months),
                            "unit_amount": {
                                "currency_code": "USD",
                                "value": str(membership.price * months)
                            }
                        }
                    ],
                    "amount": {
                        "currency_code": "USD",
                        "value": str(membership.price * months),
                        "breakdown": {
                            "item_total": {
                                "currency_code": "USD",
                                "value": str(membership.price * months),
                            }
                        }
                    }
                }
            ]
        }

        response = requests.post(
            "https://api-m.sandbox.paypal.com/v2/checkout/orders", headers=headers, data=json.dumps(data))
        print(response.status_code)
        if response.status_code == 201:
            return Response({
                "message": "successfully initialized your subscription",
                "data": response.json()
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "the payment gateway refused to initialize your subscription, try again later"
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while initiating the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST",])
@permission_classes([UserActive])
def finalize_subscription(request):
    data = request.data
    user = request.user
    paypal_confirm_url = f'https://api.sandbox.paypal.com/v2/checkout/orders/{data["subscription_id"]}'

    if not data:
        return Response({
            "message": "No data to initiate the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("membership_name")
    months = data.get("months", 1)

    if not name:
        return Response({
            "message": "Please enter the membership name"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        membership = Membership.objects.get(name=name)
    except Membership.DoesNotExist:
        return Response({
            "message": "There's no membership with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    has_membership = UserMembership.objects.filter(
        membership=membership, subscriber=user).exists()

    if has_membership:
        return Response({
            "message": "Cannot initiate a subscription for already subscribed member"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        auth_token = get_auth_token()
        # print("after generated auth token", auth_token)
    except Exception as e:
        print("error because auth token", e)
        return Response({
            "message": "an error occurred while initiating the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = requests.get(paypal_confirm_url, headers=headers)
        print("after response", response.json())

        if response.status_code == 200:
            subscription_expiration = timezone.now() + timedelta(days=months * 30)
            UserMembership.objects.create(
                subscriber=user,
                membership=membership,
                subscription_expiration=subscription_expiration,
            )
            # * Please note that if the task fails this won't affect Django's context.
            send_notification_after_sub.delay(
                user_id=user.id, membership_name=membership.name)
            return Response({
                "message": f"You have subscribed in the membership successfully! Now you can enjoy its exclusive features"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "the payment gateway refused to finalize your subscription, try again later"
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while initiating the subscription"
        }, status=status.HTTP_400_BAD_REQUEST)
