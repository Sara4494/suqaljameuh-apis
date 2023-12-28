import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth.models import User

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        
        self.user = self.scope['user']


        if self.user.is_anonymous: 
            self.close()
            return

        self.GROUP_NAME = f'user-{self.user.id}-notification'

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )


        self.accept()

    def disconnect(self, close_code):

        if not self.user.is_anonymous: 

            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["text"]



        self.channel_layer.group_send(
            self.GROUP_NAME,{'type':'notificaiotn',"text":text}
        )


    def notification (self, event) :
        text = event['text']

        self.send(text_data=json.dumps({"text":text}))
        