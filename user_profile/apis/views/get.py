from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from user_profile.models import Profile
from django.shortcuts import get_object_or_404
from users.apis.serializers import UserSerializer
from ..serializer import ProfileSerializer
from users.models import User
from globals.password_remover import RemovePasswordFromList
from Ad.models import Ad


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def ProfileInfo(request):
    try:
        user = request.user
        profile = get_object_or_404(Profile, user=user)

        user_data = UserSerializer(user)

        data = user_data.data
        data.pop('password')

        prof_data = ProfileSerializer(profile)

        data = {
            'me': data,
            'profile': prof_data.data,
        }

        return Response(data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'error': f'there is an error : {error}'}, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def user_details(request, user_id):

    try:
        is_following = None
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({
                "message": "this user does not exists"
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            ads_count = Ad.objects.filter(user__id=user.pk).count()
        except Exception as e:
            return Response({
                "message": "an error occurred while calculating user's ads"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not request.user.is_anonymous:
            is_following = user.followers.contains(request.user)
        user_data = UserSerializer(user, many=False)

        data = user_data.data
        data.pop('password')

        data = {
            'user': data,
            'is_following': is_following,
            'ads_count': ads_count
        }

        return Response(data, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'error': f'there is an error : {error}'}, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET",])
@decorators.permission_classes([permissions.AllowAny])
def get_similar_users(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({
            "message": "user doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        users = User.objects.filter(country=user.country, rate__gt=2)
        serializer = UserSerializer(users, many=True)
        return Response({
            "data": RemovePasswordFromList(serializer.data)
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while getting similar users"
        }, status=status.HTTP_400_BAD_REQUEST)
