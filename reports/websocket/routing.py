
from .consumers import AdminNotificationConsumers
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"ws/adminnotifications/", AdminNotificationConsumers.as_asgi()),
]
