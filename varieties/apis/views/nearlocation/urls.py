from django.urls import path
from varieties.apis.views.nearlocation.create import *  
from varieties.apis.views.nearlocation.update import *
from varieties.apis.views.nearlocation.delete import *
from varieties.apis.views.nearlocation.get import  *
urlpatterns = [
    path('nearlocation/', get_nearlocation, name='get_nearlocation'),
    path('create_nearlocation', create_nearlocation, name='create_nearlocation'),
    path('update_nearlocation/<int:pk>/', update_nearlocation, name='update_nearlocation'),
    path('delete_nearlocation/<int:pk>/', delete_nearlocation, name='delete_nearlocation'),
]