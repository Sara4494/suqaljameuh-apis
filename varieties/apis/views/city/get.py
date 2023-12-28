

from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView


from varieties.models import City, Country
from varieties.apis.serializers import CitySerializer, DefualtCitySerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def city_retrieve(request, pk):
    try:
        city = City.objects.get(pk=pk)
        serializer = CitySerializer(city)
        return Response({'message': 'City retrieved successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response({'error': 'City object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetCountryCities(ListAPIView):
    serializer_class = DefualtCitySerializer
    def get(self, request, *args, **kwargs):
        # get country name to get cities in country
        country_name = request.GET.get("country_name",None)
        if not country_name:
            raise ValidationError({'error':"country_name is required"})
        country_cities = City.objects.filter(country__name=country_name)
        # serialize country cities 
        serializer = self.serializer_class(instance=country_cities,many=True)
        message = {
            'country':country_name,
            "cities":serializer.data
        }
        return Response(message,status.HTTP_200_OK)
        # Mission Done </>