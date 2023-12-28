from django.urls import path

from memberships.apis.views.featured_memberships.create import create_membership
from memberships.apis.views.featured_memberships.delete import delete_membership
from memberships.apis.views.featured_memberships.update import update_membership
from memberships.apis.views.featured_memberships.get import get_memberships 

urlpatterns = [
    path("create-membership/", create_membership),
    path("delete-membership/<str:name>/", delete_membership),
    path("update-membership/<int:membership_id>/", update_membership),
    path("get-memberships/", get_memberships),
]