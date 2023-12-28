from django.urls import path
from education.apis.views.create import publish_education_ad
from education.apis.views.update import update_education_ad

urlpatterns = [
    path("publish/", publish_education_ad),
    path("update/<int:ad_id>/", update_education_ad),
]
