from django.urls import path
from .get import get_foul_types
from .update import update_foul_type
from .delete import delete_foul_type
from .create import create_foul_type

urlpatterns = [
    path("get-all/", get_foul_types),
    path("create/", create_foul_type),
    path("update/<int:foul_type_id>/", update_foul_type),
    path("delete/<int:foul_type_id>/", delete_foul_type),
]