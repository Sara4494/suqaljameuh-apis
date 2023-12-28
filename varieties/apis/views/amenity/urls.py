from django.urls import path
from .create import*
from .delete import *
from .get import *
from .update import *
urlpatterns = [
 path('amenity/<int:pk>/update/',  amenity_update ),
    path('amenity/<int:pk>/delete/',  amenity_destroy),
    path('amenity/',  amenity_create ),
    path('amenity/<int:pk>/',  amenity_retrieve ),
]
 