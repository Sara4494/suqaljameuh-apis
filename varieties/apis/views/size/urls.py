from django.urls import path
 
from varieties.apis.views.size.get import* 
from varieties.apis.views.size.create import* 
from varieties.apis.views.size.delete import* 
from varieties.apis.views.size.update import* 

urlpatterns = [
    
    path('sizes/', get_sizes, name='get_sizes'),
    path('sizes/create/', create_size, name='create_size'),
    path('sizes/<int:pk>/update/', update_size, name='update_size'),
    path('sizes/<int:pk>/delete/', delete_size, name='delete_size'),
]