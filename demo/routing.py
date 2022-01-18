from django.urls import path
from .consumer import GraphConsumer
ws_urlpatterns = [
    path('ws/graph/',GraphConsumer.as_asgi())
]