from django.urls import path
from computers.apis.views.create import publish_ad
from computers.apis.views.update import update_ad

urlpatterns = [
    path("publish/", publish_ad),
    path("update/", update_ad),
]
