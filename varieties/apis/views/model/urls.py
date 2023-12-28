from django.urls import path
from varieties.apis.views.model.get import* 
from varieties.apis.views.model.delete import* 
from varieties.apis.views.model.create import* 
from varieties.apis.views.model.update import* 

urlpatterns = [ 
    path('create_model/', create_model, name='create_model'),
    path('delete_model/<int:pk>/', delete_model, name='delete_model'),
    path('get_models/', get_models, name='get_models'),
    path('get_models/<int:subcategory_id>/', get_subcategory_models, name='get_models'),
    path('update_model/<int:pk>/', update_model, name='update_model'),
]