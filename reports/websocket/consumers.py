from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class AdminNotificationConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_superuser:
            self.GROUP_NAME = f'admin-{self.id}-notifications'
            await self.channel_layer.group_add(
                self.GROUP_NAME, self.channel_name
            )
            print(self.channel_name)
            await self.accept()
        else:
            self.GROUP_NAME = None
            await self.close()

    async def disconnect(self, close_code):
        if self.GROUP_NAME:
            await self.channel_layer.group_discard(
                self.GROUP_NAME, self.channel_name
            )

    async def report_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def problem_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
   
        
