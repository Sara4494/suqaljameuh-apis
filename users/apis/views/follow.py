from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from users.models import User
 
from rest_framework import status,permissions
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow(request):
    try:
        user_to_follow_id = request.data.get('user_to_follow')
        user_to_follow = User.objects.get(id=user_to_follow_id)
        if request.user.followings.filter(id=user_to_follow_id).exists():
            return Response({'error': 'You already follow this user.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.followings.add(user_to_follow)
        user_to_follow.followers.add(request.user)
        return Response({'success': 'You are now following this user.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow(request):
    try:
        user_to_unfollow_id = request.data.get('user_to_unfollow')
        user_to_unfollow = User.objects.get(id=user_to_unfollow_id)
        if not user_to_unfollow.followers.filter(id=request.user.id).exists():
            return Response({'error': 'You do not follow this user.'}, status=status.HTTP_400_BAD_REQUEST)
        user_to_unfollow.followers.remove(request.user)
        request.user.followings.remove(user_to_unfollow)
        return Response({'success': 'You have unfollowed this user.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
