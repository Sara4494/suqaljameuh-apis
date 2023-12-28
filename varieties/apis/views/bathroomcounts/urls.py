from django.urls import path
from django.urls import path
from varieties.apis.views.bathroomcounts.create import *  
from varieties.apis.views.bathroomcounts.update import *
from varieties.apis.views.bathroomcounts.delete import *
from varieties.apis.views.bathroomcounts.get import  *
urlpatterns = [
    path('get_roomcounts/', get_bathroomcounts, name='bathroomcounts-list'),
    path('create_roomcounts', create_bathroomcounts, name='bathroomcounts-create'),
    path('update_roomcounts/<int:pk>/', update_bathroomcounts, name='bathroomcounts-update'),
    path('delete_roomcounts/<int:pk>/', delete_bathroomcounts, name='bathroomcounts-delete'),
]