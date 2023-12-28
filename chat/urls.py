from .apis.views import send_img, send_audio
from django.urls import path
from .apis.views.chat.user import get_chats as user_get_chat, get_messages as get_user_messages
from .apis.views.chat.admin import get_chats as admin_get_chat, get_messages as admin_get_messages
from chat.apis.views.chat.user.create import CreateChat


urlpatterns = [
    path('send/image/<str:chatuuid>/', send_img.SendImageView),
    path('send/audio/<str:chatuuid>/', send_audio.SendAudioView),

    path('user-chats/', user_get_chat.GetAllUserChats),
    path('messages/<str:chatuuid>/', get_user_messages.UserChatMessage),

    path('admin/chats/', admin_get_chat.Admin_GetAllUserChats),
    path('admin/chat/messages/<str:chatuuid>/',
         admin_get_messages.Admin_UserChatMessage),

    path("create/<int:friendid>/", CreateChat)
]
