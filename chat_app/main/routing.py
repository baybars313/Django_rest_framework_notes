from django.urls import path 
from .consumers import *

websocket_urlpattern=[
		
		path("ws/sc/", MysynConsumer.as_asgi()),
		path("ws/asc/", MyasynConsumer.as_asgi()),



]