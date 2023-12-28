from django.urls import path

from varieties.apis.views.sub_category.get import* 
from varieties.apis.views.sub_category.create import* 
from varieties.apis.views.sub_category.delete import* 
from varieties.apis.views.sub_category.update import* 
urlpatterns = [
 path('subcategories/', get_subcategories, name='get_subcategories'),
    path('subcategories/create/', create_subcategory, name='create_subcategory'),
    path('subcategories/<int:pk>/update/', update_subcategory, name='update_subcategory'),
    path('subcategories/<int:pk>/delete/', delete_subcategory, name='delete_subcategory'),
]