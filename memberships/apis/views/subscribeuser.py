from rest_framework.decorators import api_view, permission_classes
from memberships.models import FeaturedMembership, FeaturedMember
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from users.models import USER_RANKS
from globals.payment_helpers import create_charge, create_customer
from datetime import timedelta
from django.utils import timezone
from memberships.tasks import send_notification_after_sub
from globals.ad_helpers import update_user_rank

"""
1. Get the user
2. Get the membership by its name
3. Calc how many months the user want to be subscribed
4. determine the expiration date based on the given months
3. create a membership for this user associated with the given membership
"""
from django.utils.translation import gettext as _


@api_view(["POST"])
@permission_classes([UserActive])
def subscribe_featuredmembership(request):
    user = request.user
    data = request.data

    if not data:
        return Response({
            "message": _("Please fill the needed information")
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("membership_name")
    months = data.get("months", 1)
    stripe_token = data.get("stripe_token")

    if not name:
        return Response({
            "message": _("Please select your membership")
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        membership = FeaturedMembership.objects.get(name=name)
    except FeaturedMembership.DoesNotExist:
        return Response({
            "message": _("Couldn't find this membership")
        }, status=status.HTTP_404_NOT_FOUND)

    has_membership = FeaturedMember.objects.filter(subscriber=user).exists()

    if has_membership:
        return Response({
            "message": "You have already subscribed at this membership"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not stripe_token:
        return Response({
            "message": _("Please provide credit card information")
        }, status=status.HTTP_400_BAD_REQUEST)

    subscription_price = months * membership.price
    subscription_expiration = timezone.now() + timedelta(days=months * 30)

    # * Start paying out process

    """
    we want to create a customer account for many reasons:
    1. basically we wanna gather information about the user who made the transaction
    2. we also want to save the card for this customer
    """
    try:
        customer = create_customer(user, stripe_token)
    except Exception as e:
        print(_("This error from creating customer in membership!"), e)
        return Response({
            "message": "An error occurred while payment processing, please try again!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # * Charging the user, now the transaction will occur
    try:
        create_charge(customer, amount=subscription_price,
                      description="Paying a membership")
    except Exception as e:
        print("an error occurred while finalizing the transaction in membership:", e)
        return Response({
            "message": _("an error occurred while finalizing the transaction, please try again")
        }, status=status.HTTP_400_BAD_REQUEST)

    # * Now the user has paid, so now we can activate him his wanted membership
    try:
        FeaturedMember.objects.create(
            subscriber=user,
            membership=membership,
            subscription_expiration=subscription_expiration,
        )
        update_user_rank(membership, user)
        # * Please note that if the task fails this won't affect Django's context.
        send_notification_after_sub.delay(
            user_id=user.id, membership_name=membership.name)
        return Response({
            "message": _(f"You have subscribed in the membership successfully! Now you can enjoy its exclusive features")
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": _("An unexpected error occurred while activating the membership, please reach out for the support")
        }, status=status.HTTP_400_BAD_REQUEST)
