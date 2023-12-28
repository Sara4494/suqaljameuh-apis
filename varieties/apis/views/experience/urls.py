from django.urls import path
from .create import *
from .delete import *
from .get import *
from .update import *
urlpatterns = [path('experience/create/', experience_create),
               path('experience/<int:pk>/update/',  experience_update),
               path('experience/<int:pk>/delete/',  experience_destroy),
               path('experiences/', experience_retrieve)
               ]
