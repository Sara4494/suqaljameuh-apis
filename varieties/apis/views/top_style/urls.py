from django.urls import path
from varieties.apis.views.top_style.get import* 
from varieties.apis.views.top_style.create import* 
from varieties.apis.views.top_style.delete import* 
from varieties.apis.views.top_style.update import*

urlpatterns = [
 
    
    path('topstyles/', get_topstyles, name='get_topstyles'),
    path('topstyles/create/', create_topstyle, name='create_topstyle'),
    path('topstyles/<int:pk>/update/', update_topstyle, name='update_topstyle'),
    path('topstyles/<int:pk>/delete/', delete_topstyle, name='delete_topstyle'),
]
 
