from django.urls import path
from varieties.apis.views.interface.create import *  
from varieties.apis.views.interface.update import *
from varieties.apis.views.interface.delete import *
from varieties.apis.views.interface.get import  *
urlpatterns = [
    path('get_interfaces/', get_interfaces, name='get_interfaces'),
    path('create_interface', create_interface, name='create_interface'),
    path('update_interface/<int:pk>/', update_interface, name='update_interface'),
    path('delete_interface/<int:pk>/', delete_interface, name='delete_interface'),
]