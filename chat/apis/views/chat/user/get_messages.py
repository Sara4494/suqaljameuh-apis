from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from chat.models import Chat, Message
from django.shortcuts import get_object_or_404
from ....serializer import MessageSerializer, ChatSerializer


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def UserChatMessage(request, chatuuid):

    try:
        chat = Chat.objects.get(uuid=chatuuid)
    except Chat.DoesNotExist:
        return Response({
            "message": "Chat doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        messages = Message.objects.filter(chat=chat).order_by("-date")
        serializer = MessageSerializer(messages, many=True)
        chat_serializer = ChatSerializer(messages, many=False)
        return Response({
            "messages": serializer.data,
            "chat": chat_serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': f'an error accured : {e}'}, status=status.HTTP_400_BAD_REQUEST)
