from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
from varieties.apis.serializers import AmenitySerializer

 
 
from django.utils.translation import gettext as _

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def amenity_retrieve(request, pk):
    try:
        amenity = Amenity.objects.get(pk=pk)
        serializer = AmenitySerializer(amenity, many=False)
        return Response({'message': _('Amenity retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Amenity.DoesNotExist:
        return Response({'error': _('Amenity object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.utils.translation import gettext as _

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def amenities_retrieve(request):
    try:
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response({'message': _('amenities retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)