from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from getfood.consumer import GetfoodConsumer

application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'getfood$', GetfoodConsumer),
         ]
        )
    ),

})