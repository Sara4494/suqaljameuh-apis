from django.urls import path
from .create import *
from .delete import *
from .get import *
from .update import *
urlpatterns = [
    path('payment_method/create/',  payment_method_create,),
    path('payment_method/get-all/',  payment_methods_retrieve,),
    path('payment_method/<int:pk>/update/',  payment_method_update),
    path('payment_method/<int:pk>/delete/',  payment_method_destroy),
    path('payment-methods/<int:pk>/', payment_method_retrieve)
]
