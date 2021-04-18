from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from click_collector import routing as click_collector_routing
from notes import routing as note_routing


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            click_collector_routing.urlpatterns +
            note_routing.urlpatterns
        )
    ),
})
