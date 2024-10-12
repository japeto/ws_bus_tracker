from django.urls import re_path, path
from .consumer import BusLocationConsumer

websocket_urlpatterns = [
    path('ws/<str:bus_id>/position', BusLocationConsumer.as_asgi()),
]
