from django.urls import path
from varieties.apis.views.type.get import* 
from varieties.apis.views.type.create import* 
from varieties.apis.views.type.delete import* 
from varieties.apis.views.type.update import*
urlpatterns = [
  
    path('types/', get_types, name='get_types'),
    path('types/create/', create_type, name='create_type'),
    path('types/<int:pk>/update/', update_type, name='update_type'),
    path('types/<int:pk>/delete/', delete_type, name='delete_type'),
]