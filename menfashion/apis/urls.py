from django.urls import path
from menfashion.apis.views.create import publish_mens_fashion_ad
from menfashion.apis.views.update import update_mens_fashion_ad

urlpatterns = [
    path("publish/", publish_mens_fashion_ad),
    path("update/<int:ad_id>/", update_mens_fashion_ad),
]
