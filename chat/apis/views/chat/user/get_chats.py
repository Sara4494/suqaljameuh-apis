from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from chat.models import Chat
from chat.apis.serializer import ChatSerializer


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def GetAllUserChats(request) :
    
    try :
        user = request.user
        chat = Chat.objects.filter(users=user)
        
        serializer = ChatSerializer(chat,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e :
        return Response({'message':f'an error accured : {e}'},status=status.HTTP_400_BAD_REQUEST)

