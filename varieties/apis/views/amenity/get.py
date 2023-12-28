from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
from varieties.apis.serializers import AmenitySerializer

 
 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def amenity_retrieve(request, pk):
    try:
        amenity = Amenity.objects.get(pk=pk, user=request.user)
        serializer = AmenitySerializer(amenity)
        return Response({'message': 'Amenity retrieved successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Amenity.DoesNotExist:
        return Response({'error': 'Amenity object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
