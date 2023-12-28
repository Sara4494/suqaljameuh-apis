from django.urls import path
from varieties.apis.views.mechanism.create import create_mechanism
from varieties.apis.views.mechanism.update import update_mechanism
from varieties.apis.views.mechanism.delete import delete_mechanism
from varieties.apis.views.mechanism.get import get_mechanisms

urlpatterns = [
    path("create/", create_mechanism),
    path("update/<int:mechanism_id>/", update_mechanism),
    path("get-all/", get_mechanisms),
    path("delete/<int:mechanism_id>/", delete_mechanism),
]
