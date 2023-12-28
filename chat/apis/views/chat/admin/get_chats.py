from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from chat.models import Chat
from chat.apis.serializer import ChatSerializer


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def Admin_GetAllUserChats(request) :
    
    try :
    
        chat = Chat.objects.all()
        
        serializer = ChatSerializer(chat,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)

