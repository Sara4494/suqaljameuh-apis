from django.urls import path
from varieties.apis.views.site.create import *  
from varieties.apis.views.site.update import *
from varieties.apis.views.site.delete import *
from varieties.apis.views.site.get import  *

urlpatterns = [
    path('create_site/', create_site, name='create_site'),
    path('delete_site/<int:pk>/', delete_site, name='delete_site'),
    path('get_sites/', get_sites, name='get_sites'),
    path('update_site/<int:pk>/', update_site, name='update_site'),
]