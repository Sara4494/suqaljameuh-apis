from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from user_profile.models import Profile
from django.shortcuts import get_object_or_404
from users.apis.serializers import UserSerializer
from ..serializer import ProfileSerializer

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def ProfileInfo (request) : 


    try : 
        user = request.user
        profile = get_object_or_404(Profile,user=user)

        user_data = UserSerializer(user)

        data = user_data.data
        data.pop('password')

        prof_data = ProfileSerializer(profile)

        

        data = {
            'me': data,
            'profile':prof_data.data, 
        }


        return Response(data,status=status.HTTP_200_OK)
    except Exception as error :
        return Response({'error':f'there is an error : {error}'},status=status.HTTP_400_BAD_REQUEST)
