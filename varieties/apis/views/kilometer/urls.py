from django.urls import path
from varieties.apis.views.kilometer.create import *  
from varieties.apis.views.kilometer.update import *
from varieties.apis.views.kilometer.delete import *
from varieties.apis.views.kilometer.get import  *
urlpatterns = [
    path('create_kilometer/', create_kilometer, name='create_kilometer'),
    path('delete_kilometer/<int:pk>/', delete_kilometer, name='delete_kilometer'),
    path('get_kilometers/', get_kilometers, name='get_kilometers'),
    path('update_kilometer/<int:pk>/', update_kilometer, name='update_kilometer'),
]