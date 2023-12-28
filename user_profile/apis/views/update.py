from rest_framework import status, permissions ,decorators
from users.permissions import IsUserProfile
from ...models import Profile
from django.shortcuts import get_object_or_404
from ..serializer import ProfileSerializer
from rest_framework.response import Response
from rest_framework import serializers

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAuthenticated,IsUserProfile])
def ProfileUpdate(request) : 
    
    user = request.user
    user_profile = get_object_or_404(Profile,user=user)



    if request.method == "PUT" : 
        serializer = ProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid() :

            username = serializer.validated_data['username']

            prof = Profile.objects.filter(username=username)
            if prof.exists():
                if prof.first().username != user_profile.username :
                    raise serializers.ValidationError('username aready exists')

            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    