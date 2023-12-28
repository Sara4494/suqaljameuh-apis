from rest_framework.response import Response
from rest_framework import decorators, permissions, status
from ...models import Chat, Message
from django.shortcuts import get_object_or_404
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def SendImageView (request, chatuuid) :
    

    try :
        chat = get_object_or_404(Chat, uuid=chatuuid)
        data = request.data
        sender = request.user

        if 'image' not in data :
            return Response({'message':"image field cannot be empty"},status=status.HTTP_400_BAD_REQUEST)
        

        if sender not in chat.users.all() :
            return Response({'message':"current user is not in the chat group"},status=status.HTTP_400_BAD_REQUEST)


        m = Message.objects.create(
            sender = sender,
            chat = chat,
            image = data.get('image')
        )
        

        m.save()

        group_name = f'room_{chatuuid}'
        channel = get_channel_layer()


        message = {
            'sender' : sender.email,
            'sender_pic' : sender.profile.picture.url,
            'date' : f'{m.date}',
            'image' : m.image.url,
            'is_admin' : sender.is_superuser

        }    

        async_to_sync(channel.group_send)(
            group_name, {
                'type':'send_message',
                'message' : message
            }
        )

        return Response({'message':'image has been sent successfully'},status=status.HTTP_201_CREATED)
    except Exception as error :
        return Response({'message':f'an error Accured : {error}'},status=status.HTTP_400_BAD_REQUEST)
        