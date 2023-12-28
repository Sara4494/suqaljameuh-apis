from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from users.models import User
from users.apis.serializers import  UserSerializer
from rest_framework import status, permissions
from users.permissions import UserOwnerOnly
from varieties.models import Country, City
from user_profile.models import Profile

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update(request):
    try:
        if request.method == 'PUT':
            user = User.objects.get(pk=request.data['id'])
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'User updated successfully.'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST',])
@permission_classes([UserOwnerOnly, permissions.IsAuthenticated])
def update_user_data(request):
    try:
        user = User.objects.get(email=request.user.email)
    except User.DoesNotExist:
        return Response({
            "message": "Couldn't find your account"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        profile = Profile.objects.get(user__email=user.email)
    except Profile.DoesNotExist:
        return Response({
            "message": "No profile exists with this email"
        }, status=status.HTTP_404_NOT_FOUND)
    
    data = request.data

    if not data:
        return Response({
            "message": "Please provide the needed information"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    full_name = data.get("full_name")
    email = data.get("email")
    country = data.get("country")
    city = data.get("city")
    phone_number = data.get("phone_number")
    birth_date = data.get("birth_date")
    gender = data.get("gender")
    facebook_link = data.get("facebook_link")
    whatsapp_number = data.get("whatsapp_number")
    instagram_link = data.get("instagram_link")
    is_update = data.get("is_update")
    country_model = None
    city_model = None
    print(is_update)
    if country:
        try:
            country_model = Country.objects.get(name=country)
        except Country.DoesNotExist:
            return Response({
                "message": "The country Doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)

    if city:
        try:
            city_model = City.objects.get(name=city)
        except City.DoesNotExist:
            return Response({
                "message": "The city Doesn't exists"
            }, status=status.HTTP_404_NOT_FOUND)
        
        
    try:
        is_updated_user = False
        is_updated_profile = False
        
        if full_name and user.full_name != full_name:
            user.full_name = full_name
            is_updated_user = True
        
        if email and user.email != email:
            user.email = email
            is_updated_user = True

        if phone_number and user.phone_number != phone_number:
            user.phone_number = phone_number
            is_updated_user = True
        
        if gender and user.gender != gender:
            user.gender = gender
            profile.picture = f"profile-images/{gender}.png"
            is_updated_user = True
        
        if birth_date and user.birth_date != birth_date:
            user.birth_date = birth_date
            is_updated_user = True

        if country:
            try:
                country_model = Country.objects.get(name=country)
            except Country.DoesNotExist:
                return Response({
                    "message": "The country Doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            user.country = country_model
            is_updated_user = True
            

        if city:
            try:
                city_model = City.objects.get(name=city)
            except City.DoesNotExist:
                return Response({
                    "message": "The city Doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            user.city = city_model
            is_updated_user = True

        if facebook_link and profile.facebook_acc != facebook_link:
            profile.facebook_acc = facebook_link
            is_updated_profile = True

        if instagram_link and profile.instagram_acc != instagram_link:
            profile.instagram_acc = instagram_link
            is_updated_profile = True

        if whatsapp_number and profile.whatsapp != whatsapp_number:
            profile.whatsapp = whatsapp_number
            is_updated_profile = True

        if is_updated_user:
            user.save()

        if is_updated_profile:
            user.save()

        if is_updated_profile or is_updated_user:
            return Response({
                "message": "Process Done Successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Nothing to process"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while performing the process"
        }, status=status.HTTP_400_BAD_REQUEST)