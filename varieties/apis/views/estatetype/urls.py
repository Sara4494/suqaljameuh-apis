from django.urls import path
from varieties.apis.views.estatetype.create import *  
from varieties.apis.views.estatetype.update import *
from varieties.apis.views.estatetype.delete import *
from varieties.apis.views.estatetype.get import  *
urlpatterns = [
    path('create_estatetype/', create_estatetype, name='create_estatetype'),
    path('delete_estatetype/<int:pk>/', delete_estatetype, name='delete_estatetype'),
    path('get_estatetypes/', get_estatetype, name='get_estatetype'),
    path('update_estatetype/<int:pk>/', update_estatetype, name='update_estatetype'),
]