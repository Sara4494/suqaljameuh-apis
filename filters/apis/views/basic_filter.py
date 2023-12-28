from Ad.models import Ad
from Ad.apis.serializers import AdPolymorphicSerializer
from varieties.models import Country, City, Category

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def is_valid_query(param):
    return param != '' and param is not None

def filter_ads(data):
    ads = Ad.objects.all()
    category = data.get("category")
    country = data.get("country")
    city = data.get("city")
    title = data.get("title")

    if is_valid_query(category):
        ads = ads.filter(category__name=category)

    if is_valid_query(country):
        ads = ads.filter(country__name=country)

    if is_valid_query(city):
        ads = ads.filter(city__name=city)
    
    if is_valid_query(title):
        ads = ads.filter(ad_title__icontains=title)
    
    return ads

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def basic_filter(request):
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