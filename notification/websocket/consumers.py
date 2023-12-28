import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from notification.models import Notification
from notification.apis.serializers import NotificationSerializer


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

        user_notifications = Notification.objects.filter(
            to_user=self.user).order_by('-sent_at')
        serializer = NotificationSerializer(user_notifications, many=True)

        self.send(text_data=json.dumps(serializer.data))

    def disconnect(self, close_code):

        if not self.user.is_anonymous:

            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )
    # ! This code doesn't make sense as notification will be only sent from the server not the client
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     text = text_data_json["text"]

    #     self.channel_layer.group_send(
    #         self.GROUP_NAME, {'type': 'notification', "text": text}
    #     )

    def notification(self, event):
        content = event['content']
        read = event['read']
        sent_at = event['sent_at']

        self.send(text_data=json.dumps(
            {"content": content, "read": read, "sent_at": sent_at}))
