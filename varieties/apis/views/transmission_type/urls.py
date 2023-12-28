from django.urls import path
from .get import *
from varieties.apis.views.transmission_type.update import  update_transmission_type
from .delete import delete_transmission_type
from .create import create_transmission_type
urlpatterns = [
    path("get-all/", get_transmission_types),
    path("create/", create_transmission_type),
    path("update/<int:transmission_type_id>/", update_transmission_type),
    path("delete/<int:transmission_type_id>/", delete_transmission_type),
 
]