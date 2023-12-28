 
from django.urls import path
from varieties.apis.views.buildinage.create import *  
from varieties.apis.views.buildinage.update import *
from varieties.apis.views.buildinage.delete import *
from varieties.apis.views.buildinage.get import  *
urlpatterns = [
    path('create_buildinage/', create_buildingage, name='create_buildingage'),
    path('delete_buildinage/<int:pk>/', delete_buildingage, name='delete_buildingage'),
    path('get_buildinages/', get_buildingages, name='get_buildingages'),
    path('update_buildinage/<int:pk>/', update_buildingage, name='update_buildingage'),
]