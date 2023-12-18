from .consumers import *
from django.urls import path
websocket_urlpatterns = [

    path('', MyCon.as_asgi()),
]