from django.urls import path
from varieties.apis.views.material.get import* 
from varieties.apis.views.material.delete import* 
from varieties.apis.views.material.create import* 
from varieties.apis.views.material.update import* 

urlpatterns = [
    path('materials/', get_materials, name='get_materials'),
    path('materials/create/', create_material, name='create_material'),
    path('materials/<int:pk>/update/', update_material, name='update_material'),
    path('materials/<int:pk>/delete/', delete_material, name='delete_material'),
]