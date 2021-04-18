from django.urls import path

from . import consumers

urlpatterns = [
    path(
        'ws/click/',
        consumers.ClickConsumer.as_asgi(),
        name="WSClickCollector"
    ),
]
