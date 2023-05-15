from django.urls import path
from .views import *


urlpatterns = [
    path("chat/init/", init, name='init'),
    path("chat/chat/", chat, name='chat'),
    path("chat/respond/string/", respond_with_string, name='respond_with_string'),
    path("chat/respond/json/", respond_with_json, name='respond_with_json'),
    #path("store/op/", user_op, name='user_op')
]