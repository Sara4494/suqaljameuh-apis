from django.urls import path

from jobs.apis.views.jobseeker.create import create_jobseeker
from jobs.apis.views.jobseeker.get import get_all, get_offer
# from jobs.apis.views.jobseeker.update import update_offer
from jobs.apis.views.jobseeker.delete import delete_seeker

urlpatterns = [
    path('create/', create_jobseeker),
    # path('update/<int:ad_id>/', update_offer),
    path('delete/<int:offer_id>/', delete_seeker),
    path('get/', get_all),
    path('get/<int:offer_id>/', get_offer),
]
