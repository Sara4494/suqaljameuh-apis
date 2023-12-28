from django.urls import path

from jobs.apis.views.joboffer.create import create_joboffer
from jobs.apis.views.joboffer.get import get_all, get_offer
from jobs.apis.views.joboffer.update import update_offer
from jobs.apis.views.joboffer.delete import delete_offer

urlpatterns = [
    path('create/', create_joboffer),
    path('update/<int:ad_id>/', update_offer),
    path('delete/<int:offer_id>/', delete_offer),
    path('get/', get_all),
    path('get/<int:offer_id>/', get_offer),
]