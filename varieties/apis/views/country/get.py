from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Country
from varieties.apis.serializers import CountrySerializer
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get_country(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        return Response({'message': 'Country retrieved successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Country.DoesNotExist:
        return Response({'error': 'Country object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
