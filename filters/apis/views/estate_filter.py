from apartments.models import RealEstate
from Ad.apis.serializers import AdPolymorphicSerializer
from .basic_filter import is_valid_query

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def filter_ads(data):
    ads = RealEstate.objects.all()
    category = data.get("category")
    estate_type = data.get("estate_type")
    is_rental = data.get("is_rental")
    country = data.get("country")
    min_price = data.get("min_price")
    max_price = data.get("max_price")

    if is_valid_query(category):
        ads = ads.filter(category__name=category)

    if is_valid_query(estate_type):
        ads = ads.filter(estate_type__name=estate_type)

    if is_valid_query(is_rental):
        ads = ads.filter(is_rental=is_rental)

    if is_valid_query(country):
        ads = ads.filter(country__name=country)

    if is_valid_query(min_price):
        ads = ads.filter(price__gt=min_price)

    if is_valid_query(max_price):
        ads = ads.filter(price__lt=max_price)

    return ads


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def estate_filter(request):
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
