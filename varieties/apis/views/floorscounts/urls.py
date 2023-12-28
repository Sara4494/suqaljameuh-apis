 
from django.urls import path
from varieties.apis.views.floorscounts.create import *  
from varieties.apis.views.floorscounts.update import *
from varieties.apis.views.floorscounts.delete import *
from varieties.apis.views.floorscounts.get import  *
urlpatterns = [
    path('create_floorscounts/', create_floorscounts, name='create_floorscounts'),
    path('delete_floorscounts/<int:pk>/', delete_floorscounts, name='delete_floorscounts'),
    path('get_floorscountss/', get_floorscounts, name='get_floorscounts'),
    path('update_floorscounts/<int:pk>/', update_floorscounts, name='update_floorscounts'),
]