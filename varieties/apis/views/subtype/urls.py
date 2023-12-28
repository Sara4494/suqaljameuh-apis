from django.urls import path
from varieties.apis.views.subtype.create import *  
from varieties.apis.views.subtype.update import *
from varieties.apis.views.subtype.delete import *
from varieties.apis.views.subtype.get import  *
urlpatterns = [
   
    path('create_subtype/', create_subtype, name='create_subtype'),
    path('delete_subtype/<int:pk>/', delete_subtype, name='delete_subtype'),
    path('get_subtypes/', get_subtypes, name='get_subtypes'),
    path('update_subtype/<int:pk>/', update_subtype, name='update_subtype'),
]