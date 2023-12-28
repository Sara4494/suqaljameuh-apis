from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
# nopep8
import notification.websocket.routing
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from notification.websocket.routing import websocket_urlpatterns as notification_websocket_urlpatterns
from chat.websocket.routing import websocket_urlpatterns as chat_websocket_urlpatterns
import reports.websocket.routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from core.middleware import TokenAuthMiddleware


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(URLRouter(
                chat_websocket_urlpatterns +
                notification.websocket.routing.websocket_urlpatterns +
                reports.websocket.routing.websocket_urlpatterns
            )
            )
        ),
    })
