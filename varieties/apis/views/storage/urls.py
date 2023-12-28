from django.urls import path
from varieties.apis.views.storage.create import *  
from varieties.apis.views.storage.update import *
from varieties.apis.views.storage.delete import *
from varieties.apis.views.storage.get import  *
urlpatterns = [
    path('create_storage/', create_storage, name='create_storage'), 
    path('delete_storage/<int:pk>/', delete_storage, name='delete_storage'),
    path('get_storages/', get_storages, name='get_storages'),
    path('update_storage/<int:pk>/', update_storage, name='update_storage'),
     
]