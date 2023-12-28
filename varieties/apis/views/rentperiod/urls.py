from django.urls import path
from varieties.apis.views.rentperiod.create import create_rent_period
from varieties.apis.views.rentperiod.update import *
from varieties.apis.views.rentperiod.delete import *
from varieties.apis.views.rentperiod.get import  *

urlpatterns = [
   path('create_rent_period/',  create_rent_period, name='create_rent_period'),
    path('delete_rent_period/<int:pk>/',  delete_rent_period, name='delete_rent_period'),
    path('get_rent_periods/',  get_rent_periods, name='get_rent_periods'),
    path('update_rent_period/<int:pk>/',  update_rent_period, name='update_rent_period'),
]