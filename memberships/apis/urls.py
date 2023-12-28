from django.urls import path, include
from memberships.apis.views.subscribeuser import *
from memberships.apis.views.subscribe import subscribe_membership, test_membership
from memberships.apis.views.create import create_membership
from memberships.apis.views.delete import delete_membership
from memberships.apis.views.update import update_membership
from memberships.apis.views.get import get_memberships 
urlpatterns = [
    path("feature-user/", subscribe_featuredmembership),
    path("subscribe/", subscribe_membership),
    path("test-subscribe/", test_membership),
    path("create-membership/", create_membership),
    path("delete-membership/<str:name>/", delete_membership),
    path("update-membership/<int:membership_id>/", update_membership),
    path("get-memberships/", get_memberships),
    path('ad-memberships/', include("memberships.apis.views.ad_memberships.urls")),
    path('featured-memberships/', include("memberships.apis.views.featured_memberships.urls")),
    path("subscribe-paypal/", include("memberships.apis.views.paypal.urls"))
]

