from rest_framework.response import Response
from rest_framework import decorators, permissions, status
from ...models import Chat, Message
from django.shortcuts import get_object_or_404
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync




@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def SendAudioView (request, chatuuid) :
    

    try :
        chat = get_object_or_404(Chat, uuid=chatuuid)
        data = request.data
        sender = request.user

        if 'audio' not in data :
            return Response({'message':"audio field cannot be empty"},status=status.HTTP_400_BAD_REQUEST)
        

        if sender not in chat.users.all() :
            return Response({'message':"current user is not in the chat group"},status=status.HTTP_400_BAD_REQUEST)


        m = Message.objects.create(
            sender = sender,
            chat = chat,
            audio = data.get('audio')
        )
        

        m.save()

        group_name = f'room_{chatuuid}'
        channel = get_channel_layer()


        message = {
            'sender' : sender.email,
            'sender_pic' : sender.profile.picture.url,
            'date' : f'{m.date}',
            'audio' : m.audio.url,
            'is_admin' : sender.is_superuser
        }


        async_to_sync(channel.group_send)(
            group_name, {
                'type':'send_message',
                'message' : message
            }
        )

        return Response({'message':'audio has been sent successfully'},status=status.HTTP_201_CREATED)
    except Exception as error :
        return Response({'message':f'an error Accured : {error}'},status=status.HTTP_400_BAD_REQUEST)

