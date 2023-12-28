from django.urls import path
from .create import *
from .delete import *
from .get import *
from .update import *
urlpatterns = [
    path('city/create/', city_create, name='city_create'),
    path('city/<int:pk>/update/', city_update, name='city_update'),
    path('city/<int:pk>/delete/',  city_destroy, name='city_destroy'),
    path('city/<int:pk>/',  city_retrieve, name='city_retrieve'),
    path("cities/<str:country_name>/", get_all_country_cities),
    path("cities/", get_all_cities)
]
