from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.permissions import UserActive
from memberships.models import AdMembership, UserMembership
from varieties.models import SubCategory, Currency, Country, City, Brand, Type, Size, Colors, Condition, PaymentMethod
from Ad.models import Ad
from Ad.apis.serializers import AdSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


@api_view(["POST",])
@permission_classes([permissions.AllowAny])
def search_ads(request):
    data = request.data

    if not data:
        return Response({
            "message": "Please fill the information to get you what you want!"
        }, status=status.HTTP_400_BAD_REQUEST)

    keywords = data.get("keywords", "")
    excluded_words = data.get("excluded_words", "")
    category = data.get("category", "")
    condition = data.get("condition", "")
    country = data.get("country", "")
    city = data.get("city", "")
    least_price = data.get("least_price")
    max_price = data.get("max_price")

    try:
        condition_model = Condition.objects.get(name=condition)
    except Condition.DoesNotExist:
        return Response({
            "message": "Couldn't find the condition you want"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        vector = SearchVector("ad_title", "ad_description")
        query = SearchQuery(keywords)
        filtered_ads = Ad.objects.annotate(
            rank=SearchRank(vector, query)).filter(
            category__category__name=category, country__name=country, city__name=city, condition=condition_model, price_gte=least_price, price_lte=max_price).exclude(ad_title__icontains=excluded_words).order_by('-rank')
        for r in filtered_ads:
            print(r.rank)
        serializer = AdSerializer(filtered_ads, many=True).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while searching in the ads, please make sure to enter a valid data"
        }, status=status.HTTP_400_BAD_REQUEST)
