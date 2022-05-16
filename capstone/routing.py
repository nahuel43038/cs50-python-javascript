from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',
            consumers.CapstoneRoomConsumer.as_asgi()),
    path('ws/private_room/<str:room_name>/',
         consumers.ChatPrivateConsumer.as_asgi()),
    path('ws/private/pre_room/<str:room_name>_<int:user_id>',
         consumers.PreRoomPrivateConsumer.as_asgi()),
    path('ws/private/<int:id>/<int:user>',
         consumers.PersonalChatConsumer.as_asgi()),
]
