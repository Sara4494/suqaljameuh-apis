from django.urls import path, include

urlpatterns = [
    path('job-offers/', include('jobs.apis.views.joboffer.urls')),
    path('job-seekers/', include('jobs.apis.views.jobseeker.urls')),
]