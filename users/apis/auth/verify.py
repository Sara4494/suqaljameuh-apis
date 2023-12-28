from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from users.models import OTPCode
from users.apis.auth.user.login import generate_token
from django.utils import timezone
from users.tasks import send_verification_notification
now = timezone.now()


@api_view(["POST",])
def verify_otp(request):
    data = request.data

    if not data:
        return Response({
            "message": "Please enter the OTP code to activate your account"
        }, status=status.HTTP_400_BAD_REQUEST)

    otp_code = data.get("otp_code")
    email = data.get("email")

    if not otp_code:
        return Response({
            "message": "Please enter the OTP code to activate your account"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not email:
        return Response({
            "message": "Email not found"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({
            "message": "There's no user matches this user"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        otp = OTPCode.objects.filter(user=user).last()
        if not otp:
            return Response({
                "message": "We didn't detect any OTP code that was sent to you lately"
            }, status=status.HTTP_400_BAD_REQUEST)
        if now > otp.valid_for:
            otp.delete()
            return Response({
                "message": "The OTP You're Trying to enter is no longer active"
            }, status=status.HTTP_400_BAD_REQUEST)

        if otp.otp != otp_code:
            return Response({
                "message": "OTP isn't correct"
            }, status=status.HTTP_400_BAD_REQUEST)
        user.verified = True
        user.save()
        otp.delete()
        tokens = generate_token(user)
        send_verification_notification.delay(email=user.email)
        return Response({
            "message": "Congrats! your account has been fully activated and you can now leverage",
            "data": tokens
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while activating your account, contact support or click on resend button"
        }, status=status.HTTP_400_BAD_REQUEST)
