from django.urls import path
from varieties.apis.views.memory.create import *  
from varieties.apis.views.memory.update import *
from varieties.apis.views.memory.delete import *
from varieties.apis.views.memory.get import  *

urlpatterns = [
    path('create_memory/',  create_memory, name='create_memory'),
    path('delete_memory/<int:pk>/',  delete_memory, name='delete_memory'),
    path('get_memories/',  get_memories, name='get_memories'),
    path('update_memory/<int:pk>/',  update_memory, name='update_memory'),
]