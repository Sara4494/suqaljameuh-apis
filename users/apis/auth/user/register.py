from django.contrib.auth.hashers import make_password
from rest_framework import decorators, status
from rest_framework.response import Response
from user_profile.models import Profile
from users.models import User
from varieties.models import Country, City
from users.tasks import send_otp


@decorators.api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    password = data.get("password")
    full_name = data.get('full_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    city = data.get('city')
    country = data.get('country')
    gender = data.get('gender')
    birth_date = data.get('birth_date')
    country_model = None
    city_model = None

    if not data:
        return Response({
            "message": "Please enter the needed information to create your account"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not username:
        return Response({
            "message": "Please enter your username"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({
            "message": "Please enter your password"
        }, status=status.HTTP_400_BAD_REQUEST)

    if len(password) < 6 or len(password) > 16:
        return Response({
            "message": "The password must be within 6 to 16 words"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not full_name:
        return Response({
            "message": "Please enter your full name"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not email:
        return Response({
            "message": "Please enter your email"
        }, status=status.HTTP_400_BAD_REQUEST)

    email_exists = User.objects.filter(email=email).exists()

    if email_exists:
        user_exists = User.objects.get(email=email)
        print(user_exists.verified)
        if user_exists.verified == True:
            return Response({
                "message": "This user is already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        if user_exists.verified == False:
            send_otp.delay(email=user_exists.email)
            return Response({
                "message": "We have found your account and sent OTP code to your email"
            }, status=status.HTTP_200_OK)

    if country:
        try:
            country_model = Country.objects.get(name=country)
        except Country.DoesNotExist:
            return Response({
                "message": "this country doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)

    if city:
        try:
            city_model = City.objects.get(name=city)
        except City.DoesNotExist:
            return Response({
                "message": "this city doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            birth_date=birth_date,
            country=country_model,
            city=city_model,
            gender=gender,
            password=make_password(password)
        )

        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return Response({
                "message": "could't find your profile"
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            profile.username = username
            profile.save()
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while setting your username"
            }, status=status.HTTP_404_NOT_FOUND)
        print(user)
        send_otp.delay(email=user.email)
        return Response({
            "message": "Your account has been created and waiting for OTP verification"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while creating your account"
        }, status=status.HTTP_400_BAD_REQUEST)
