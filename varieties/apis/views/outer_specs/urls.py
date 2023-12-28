from django.urls import path
from .get import get_outer_specs
from .update import update_outer_specs
from .delete import delete_outer_specs
from .create import create_outer_specs
urlpatterns = [
    path("outer-specs/get-all/", get_outer_specs),
    path("outer-specs/create/", create_outer_specs),
    path("outer-specs/update/<int:outer_specs_id>/", update_outer_specs),
    path("outer-specs/delete/<int:outer_specs_id>/", delete_outer_specs),
]