from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/webcam/', consumers.WebcamConsumer.as_asgi()),
]

