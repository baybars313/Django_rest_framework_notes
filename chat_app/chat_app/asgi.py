import os

from channels.routing import ProtocolTypeRouter,  URLRouter
from django.core.asgi import get_asgi_application
import main.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chant_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
    	main.routing.websocket_urlpattern

    	)
    # Just HTTP for now. (We can add other protocols later.)
})