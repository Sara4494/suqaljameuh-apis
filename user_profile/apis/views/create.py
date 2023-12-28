from rest_framework import permissions,status, decorators
from ..serializer import ProfileSerializer
from users.permissions import IsUserProfile
from ...models import Profile
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers

@decorators.api_view(['POST'])
@decorators.permission_classes([IsUserProfile, permissions.IsAuthenticated])
def CreateProfile (request) : 
    user_profile = get_object_or_404(Profile, user = request.user)
    serializer = ProfileSerializer(user_profile,data=request.data)

    if serializer.is_valid():
        
        username = serializer.validated_data['username']

        if Profile.objects.filter(username=username).exists():
            raise serializers.ValidationError('username aready exists')

        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

