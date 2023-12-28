from users.models import User, OTPCode
from rest_framework import decorators, status
from rest_framework.response import Response
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from globals.mailer import send_email
from notification.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task(bind=False)
def send_otp(email):
    try:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("Couldn't find the user")
        code = OTPCode.objects.create(
            user=user,
            valid_for=timezone.now() + timedelta(minutes=3)
        )
        print("code created")
        message = f"Welcome in Suqaljameuh! this your OTP code: {code.otp}, please use it to verify your identity and complete creating your account without this OTP we won't be able to authorize you and your account will remain inactive"
        send_email.delay(subject="Suqaljameuh Registration OTP",
                         message=message, email=user.email)
    except Exception as e:
        print("an error occurred while sending the user the OTP", e)


@shared_task(bind=False)
def send_verification_notification(email):
    try:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("Couldn't find the user")

        try:
            notification = Notification.objects.create(
                to_user=user,
                content="Thanks For Verifying Your Identity, Now You Can Enjoy Using Our Service!"
            )
            notification_event = {
                "content": notification.content,
                "read": notification.read,
                "sent_at": notification.sent_at,
                "type": "notification"
            }
            notification_channel = f"user-{user.pk}-notification"
            layers = get_channel_layer()
            async_to_sync(layers.group_send)(
                notification_channel, notification_event
            )
        except Exception as e:
            print("an error occurred while sending the notification to the user", e)
    except Exception as e:
        print("an error occurred while sending the user a verification notification", e)
