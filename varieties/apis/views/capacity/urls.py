from django.urls import path
from django.urls import path
from varieties.apis.views.capacity.create import *
from varieties.apis.views.capacity.update import *
from varieties.apis.views.capacity.delete import *
from varieties.apis.views.capacity.get import  *

urlpatterns = [
    path('create_capacity/',  create_capacity, name='create_capacity'),
    path('delete_capacity/<int:pk>/',  delete_capacity, name='delete_capacity'),
    path('get_capacities/',  get_capacities, name='get_capacities'),
    path('get_capacities/',  get_capacities, name='get_capacities'),
    path('update_capacity/<int:pk>/',  update_capacity, name='update_capacity'),
]
 