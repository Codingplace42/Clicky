from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/click', consumers.ClickConsumer.as_asgi()),
]
