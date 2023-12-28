from django.urls import path
from .create import*
from .delete import *
from .get import *
from .update import *
urlpatterns = [
    path('qualification/create/', qualification_create ),
    path('qualification/<int:pk>/update/', qualification_update  ),
    path('qualification/<int:pk>/delete/',  qualification_destroy ),
      path('qualification/<int:pk>/', qualification_retrieve ),
]