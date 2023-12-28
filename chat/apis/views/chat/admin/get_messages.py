from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from chat.models import Chat, Message
from django.shortcuts import get_object_or_404
from ....serializer import AdminMessageSerializer

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def Admin_UserChatMessage(request, chatuuid) :
    
    try :
        chat = get_object_or_404(Chat,uuid=chatuuid)

        messages = Message.objects.filter(chat=chat)
        
        serializer = AdminMessageSerializer(messages, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)
