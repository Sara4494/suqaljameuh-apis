from django.urls import path
from  .create import *

urlpatterns = [
    path('make_reports/', make_reports, name='make_reports'),
]