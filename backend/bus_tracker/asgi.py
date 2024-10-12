
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.bus import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bus_tracker.settings')
# print("#####  ProtocolTypeRouter", )

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(routing.websocket_urlpatterns),
})

