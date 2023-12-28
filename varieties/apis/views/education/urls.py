from django.urls import path
from .create import *
from .delete import *
from .get import *
from .update import *
urlpatterns = [
    path('education/create/',  education_create),
    path('education/<int:pk>/update/', education_update),
    path('education/<int:pk>/delete/',  education_destroy),
    path('educations/', education_retrieve),
]
