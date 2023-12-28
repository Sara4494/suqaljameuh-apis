from django.urls import path
from .get import get_internal_specs
from .update import update_internal_specs
from .delete import delete_internal_specs
from .create import create_internal_specs

urlpatterns = [
    path("get-all/", get_internal_specs),
    
    path("create-internal-specs/", create_internal_specs),
    path("delete-internal-specs/<int:internal_specs_id>/", delete_internal_specs),
     
    path("update-internal-specs/<int:internal_specs_id>/", update_internal_specs),
]
 