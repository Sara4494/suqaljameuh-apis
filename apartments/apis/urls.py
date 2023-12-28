from django.urls import path
from apartments.apis.views.create import publish_ad
from apartments.apis.views.update import update_ad


urlpatterns = [
    path("publish/", publish_ad),
    path("update/", update_ad),
]
