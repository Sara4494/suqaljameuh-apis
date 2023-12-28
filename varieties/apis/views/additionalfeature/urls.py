from django.urls import path
from varieties.apis.views.additionalfeature.create import *  
from varieties.apis.views.additionalfeature.update import *
from varieties.apis.views.additionalfeature.delete import *
from varieties.apis.views.additionalfeature.get import  *


urlpatterns = [
    path('create_additionalfeature/', create_additional_feature, name='create_additional_feature'),
    path('delete_additionalfeature/<int:pk>/', delete_additional_feature, name='delete_additional_feature'),
    path('get_additionalfeature/', get_additional_features, name='get_additional_features'),
    path('update_additionalfeature/<int:pk>/', update_additional_feature, name='update_additional_feature'),
]