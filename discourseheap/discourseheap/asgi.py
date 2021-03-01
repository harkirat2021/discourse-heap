import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import discussions.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discourseheap.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            discussions.routing.websocket_urlpatterns
        )
    ),
})