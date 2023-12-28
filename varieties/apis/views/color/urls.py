from django.urls import path
from varieties.apis.views.color.create import  *
from varieties.apis.views.color.get import  *
from varieties.apis.views.color.update import  *
from varieties.apis.views.color.delete import  *

urlpatterns = [
    path('colors/',  GetColor.as_view(), name='get_color'),
    path('colors/create/',  CreateColor.as_view(), name='create_color'),
    path('colors/<int:pk>/update/',  UpdateColor.as_view(), name='update_color'),
    path('colors/<int:pk>/delete/',  DeleteColor.as_view(), name='delete_color'),
]