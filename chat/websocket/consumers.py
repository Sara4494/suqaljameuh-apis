from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from chat.models import Chat, Message


class Online_Offline_Consumer (WebsocketConsumer):

    def connect(self):

        self.user = self.scope['user']

        if self.user.is_anonymous:
            print("Yes he is")
            self.close()
            return

        self.accept()

        self.user.is_online = True
        self.user.save()

    def disconnect(self, code):
        if not self.user.is_anonymous:
            self.user.is_online = False
            self.user.save()


class ChatConsumer (WebsocketConsumer):

    def connect(self):

        self.user = self.scope['user']
        chat_uuid = self.scope['url_route']['kwargs']['chatuuid']

        if self.user.is_anonymous:
            print("Yes he is")
            self.close()
            return

        try:
            print("Yes he is (Chat)")
            self.chat = Chat.objects.get(uuid=chat_uuid)
        except Chat.DoesNotExist:
            self.close()

        self.accept()
        self.GROUP_NAME = f'room_{chat_uuid}'

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )

    def receive(self, text_data):
        json_data = json.loads(text_data)
        print("data", json_data)
        msg = Message.objects.create(
            text=json_data['message'],
            sender=self.user,
            chat=self.chat
        )

        msg.save()

        json_data['sender'] = msg.sender.email
        json_data['sender_pic'] = msg.sender.profile.picture.url
        json_data['date'] = f'{msg.date}'
        json_data['is_me'] = bool(msg.sender == self.user)

        async_to_sync(self.channel_layer.group_send)(
            self.GROUP_NAME, {
                'type': 'send_message',
                'message': json_data
            }
        )

    def disconnect(self, code):
        if not self.user.is_anonymous:
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )

    def send_message(self, event):
        self.send(text_data=json.dumps(event['message']))
