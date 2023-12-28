from django.urls import path
from .get import get_body_types
 
 
from .update import update_body_type
from .delete import delete_body_type
from .create import create_body_type

urlpatterns = [
    path("get-all/", get_body_types),
       path("body-type/create/", create_body_type),
    path("body-type/update/<int:body_type_id>/", update_body_type),
    path("body-type/delete/<int:body_type_id>/", delete_body_type),
]