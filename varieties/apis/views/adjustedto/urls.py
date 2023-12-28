from django.urls import path
from varieties.apis.views.adjustedto.create import *  
from varieties.apis.views.adjustedto.update import *
from varieties.apis.views.adjustedto.delete import *
from varieties.apis.views.adjustedto.get import  *

urlpatterns = [
    path('get_adjustedtos/', get_adjustedto, name='get_adjustedto'),
    path('create_adjustedto/', create_adjustedto, name='create_adjustedto'),
    path('update_adjustedto/<int:pk>/', update_adjustedto, name='update_adjustedto'),
    path('delete_adjustedto/<int:pk>/', delete_adjustedto, name='delete_adjustedto'),
]