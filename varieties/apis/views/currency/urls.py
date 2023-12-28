from django.urls import path
from .create import*
from .delete import *
from .get import *
from .update import *
urlpatterns = [ 
     path('currency/create/',create_currency ),
    path('currency/<int:pk>/update/',  update_currency ),
    path('currency/<int:pk>/delete/',  delete_currency ),
      path('currencies/<int:pk>/', currency_detail)

    ]
