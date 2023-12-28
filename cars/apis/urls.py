from django.urls import path
from cars.apis.views.create import publish_ad
from cars.apis.views.update import update_ad

urlpatterns = [
    path("publish/", publish_ad),
    path("update/", update_ad),
]
