from django.urls import path
from electronics.apis.views.create import publish_ad
from electronics.apis.views.update import update_ad

urlpatterns = [
    path("publish/", publish_ad),
    path("update/<int:ad_id>/", update_ad),
]
