from django.urls import path
from .get import get_regional_specs
 
from .update import update_regional_specs
from .delete import delete_regional_specs
from .create import create_regional_specs
urlpatterns = [
    path("get-all/", get_regional_specs),
    path("regional-specs/create/", create_regional_specs),
    path("regional-specs/update/<int:regional_specs_id>/", update_regional_specs),
    path("regional-specs/delete/<int:regional_specs_id>/", delete_regional_specs),
]