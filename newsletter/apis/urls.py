 
from django.urls import path  
from  .views.tasks import *
from .views.subscribe import *
urlpatterns = [
    path('newsletter/', send_top_rated_news),
    path('subscribe/', subscribe),

]