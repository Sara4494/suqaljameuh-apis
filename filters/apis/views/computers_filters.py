from computers.models import Computer
from Ad.apis.serializers import AdPolymorphicSerializer
from .basic_filter import is_valid_query

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def filter_ads(data):
    ads = Computer.objects.all()
    category = data.get("category")
    country = data.get("country")
    city = data.get("city")
    brand = data.get("brand")
    screen_size = data.get("screen_size")
    storage = data.get("storage")
    colors = data.get("colors")
    os = data.get("os")
    memory = data.get("memory")
    rating = data.get("rating")
    condition = data.get("condition")
    min_price = data.get("min_price")
    max_price = data.get("max_price")

    if is_valid_query(category):
        ads = ads.filter(category__name=category)

    if is_valid_query(city):
        ads = ads.filter(city__name=city)

    if is_valid_query(country):
        ads = ads.filter(country__name=country)

    if is_valid_query(brand):
        ads = ads.filter(brand__name=brand)

    if is_valid_query(screen_size):
        ads = ads.filter(screen_size__name=screen_size)

    if is_valid_query(colors):
        ads = ads.filter(color__in=colors)

    if is_valid_query(os):
        ads = ads.filter(os__in=os)

    if is_valid_query(memory):
        ads = ads.filter(memory__in=memory)

    if is_valid_query(rating):
        ads = ads.filter(rating__in=rating)

    if is_valid_query(condition):
        ads = ads.filter(condition__in=condition)

    if is_valid_query(storage):
        ads = ads.filter(storage__name=storage)

    if is_valid_query(max_price):
        ads = ads.filter(price__lt=max_price)

    if is_valid_query(min_price):
        ads = ads.filter(price__gt=min_price)

    return ads


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def computer_filter(request):
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
