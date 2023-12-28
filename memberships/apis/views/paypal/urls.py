from django.urls import path
from .membership import initiate_subscription, finalize_subscription
from .feautre_membership import initiate_subscription, finalize_subscription

urlpatterns = [
    path("init-subscription/", initiate_subscription),
    path("finalize-subscription/", finalize_subscription),
    path("init-feature-subscription/", initiate_subscription),
    path("finalize-feature-subscription/", finalize_subscription),
]