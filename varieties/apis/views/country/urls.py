from django.urls import path
from .create import *
from .delete import *
from .get import *
from .update import *
urlpatterns = [
    path('country/create/',  create_country, name='country_create'),
    path('country/<int:pk>/update/',  update_country, name='country_update'),
    path('country/<int:pk>/delete/',  delete_country, name='country_destroy'),
    path('country/<int:pk>/', get_country, name='get_country'),
    path('countries/', get_countries, name='get_countries'),
]
