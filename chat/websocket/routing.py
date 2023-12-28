from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path("chat/<str:chatuuid>/", consumers.ChatConsumer.as_asgi()),
    path('online/',consumers.Online_Offline_Consumer.as_asgi()),
]