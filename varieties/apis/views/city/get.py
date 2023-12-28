

from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView


from varieties.models import City, Country
from varieties.apis.serializers import CitySerializer, DefualtCitySerializer
from django.utils.translation import gettext as _


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def city_retrieve(request, pk):
    try:
        city = City.objects.get(pk=pk)
        serializer = CitySerializer(city)
        return Response({'message': _('City retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response({'error': _('City object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_all_country_cities(request, country_name):
    try:
        country = Country.objects.get(name=country_name)
    except Country.DoesNotExist:
        return Response({
            "message": "there's no country with this name"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        cities = City.objects.filter(country=country)
        data = CitySerializer(cities, many=True)
        return Response({
            "data": data.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while retrieving the cities"
        }, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_all_cities(request):
    try:
        cities = City.objects.all()
        data = CitySerializer(cities, many=True)
        return Response({
            "data": data.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while retrieving the cities"
        }, status=status.HTTP_400_BAD_REQUEST)
 
