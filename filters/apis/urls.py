from django.urls import path
from filters.apis.views.basic_filter import basic_filter
from filters.apis.views.computers_filters import computer_filter
from filters.apis.views.estate_filter import estate_filter
from filters.apis.views.cars_filters import cars_filter
from filters.apis.views.education import education_filter
from filters.apis.views.fashion import fashion_filter
from filters.apis.views.motorbikes_filters import motorbikes_filters
from filters.apis.views.electronics_filters import electronics_filter

urlpatterns = [
    path("basic-filter/", basic_filter),
    path("computer-filter/", computer_filter),
    path("estate-filter/", estate_filter),
    path("cars-filter/", cars_filter),
    path("eduction-filter/", education_filter),
    path("fashion-filter/", fashion_filter),
    path("motorbikes-filter/", motorbikes_filters),
    path("electronics-filter/", electronics_filter),
]