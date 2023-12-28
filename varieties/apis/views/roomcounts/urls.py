from django.urls import path
from varieties.apis.views.roomcounts.create import *  
from varieties.apis.views.roomcounts.update import *
from varieties.apis.views.roomcounts.delete import *
from varieties.apis.views.roomcounts.get import  *
urlpatterns = [
    path('get_roomcountss/', get_roomcounts, name='roomcounts-list'),
    path('create_roomcounts', create_roomcounts, name='roomcounts-create'),
    path('update_roomcounts/<int:pk>/', update_roomcounts, name='roomcounts-update'),
    path('delete_roomcounts/<int:pk>/', delete_roomcounts, name='roomcounts-delete'),
]