from cars.models import Car
from Ad.apis.serializers import AdPolymorphicSerializer
from .basic_filter import is_valid_query

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def filter_ads(data):
    ads = Car.objects.all()
    category = data.get("category")
    country = data.get("country")
    city = data.get("city")
    title = data.get("title")
    transmission_type = data.get("transmission_type")
    body_type = data.get("body_type")
    foul_type = data.get("foul_type")
    internal_specs = data.get("internal_specs")
    external_specs = data.get("external_specs")
    regional_specs = data.get("regional_specs")
    car_number = data.get("car_number")
    kilo_meter = data.get("kilo_meter")
    is_rental = data.get("is_rental")
    rent_period = data.get("rent_period")
    min_price = data.get("min_price")
    max_price = data.get("max_price")

    if is_valid_query(category):
        ads = ads.filter(category__name=category)

    if is_valid_query(title):
        ads = ads.filter(ad_title__icontains=title)

    if is_valid_query(city):
        ads = ads.filter(city__name=city)

    if is_valid_query(country):
        ads = ads.filter(country__name=country)

    if is_valid_query(transmission_type):
        ads = ads.filter(transmission_type__name=transmission_type)

    if is_valid_query(body_type):
        ads = ads.filter(body_type__name=body_type)

    if is_valid_query(foul_type):
        ads = ads.filter(foul_type__in=foul_type)

    if is_valid_query(internal_specs):
        ads = ads.filter(internal_specs__in=internal_specs)

    if is_valid_query(external_specs):
        ads = ads.filter(external_specs__in=external_specs)

    if is_valid_query(regional_specs):
        ads = ads.filter(regional_specs__in=regional_specs)

    if is_valid_query(car_number):
        ads = ads.filter(car_number__in=car_number)

    if is_valid_query(kilo_meter):
        ads = ads.filter(kilo_meter__in=kilo_meter)

    if is_valid_query(is_rental):
        ads = ads.filter(is_rental__name=is_rental)

    if is_valid_query(rent_period):
        ads = ads.filter(rent_period__name=rent_period)

    if is_valid_query(max_price):
        ads = ads.filter(price__lt=max_price)

    if is_valid_query(min_price):
        ads = ads.filter(price__gt=min_price)

    return ads


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def cars_filter(request):
    try:
        ads = filter_ads(request.data)
        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages

        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while filtering the ads"
        }, status=status.HTTP_400_BAD_REQUEST)
