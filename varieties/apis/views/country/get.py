from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Country
from varieties.apis.serializers import CountrySerializer
 
from django.utils.translation import gettext as _
 
 


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_country(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        return Response({'message': _('Country retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Country.DoesNotExist:
        return Response({'error': _('ountry object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_countries(request):
    try:
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response({'message': _('Countries retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)