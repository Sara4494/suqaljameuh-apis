from django.urls import path
from  .views.create import  *
from  .views.delete import  delete
from  .views.get import  get
from  .views.update import  update
from .views.follow import *
 
urlpatterns = [
     
    path('create/', create ),
    path('delete/', delete ),
    path('get/', get ),
    path('update/', update ),
    path('follow/', follow),
    path('unfollow/', unfollow)
]