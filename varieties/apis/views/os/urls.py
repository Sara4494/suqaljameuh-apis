from django.urls import path
from varieties.apis.views.os.create import *  
from varieties.apis.views.os.update import *
from varieties.apis.views.os.delete import *
from varieties.apis.views.os.get import  *
urlpatterns = [
    path('create_os/',  create_os, name='create_os'),
    path('delete_os/<int:pk>/',  delete_os, name='delete_os'),
    path('get_oss/',  get_oss, name='get_oss'),
    path('update_os/<int:pk>/',  update_os, name='update_os'),
]