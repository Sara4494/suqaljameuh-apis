from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from chat.models import Chat
from django.shortcuts import get_object_or_404
from users.models import User


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def CreateChat(request, friendid):

    try:
        friend = get_object_or_404(User, id=friendid)

        user = request.user

        if user == friend:
            return Response({'message': 'please enter a valid friend id'}, status=status.HTTP_400_BAD_REQUEST)

        chat = Chat.objects.create()
        # exists = Chat.objects.contains(user, friend)
        chat.users.add(user)
        chat.users.add(friend)

        chat.save()

        response = {
            'chatuuid': f'{chat.uuid}',
        }

        return Response(response, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': f'an error accured : {e}'}, status=status.HTTP_400_BAD_REQUEST)
