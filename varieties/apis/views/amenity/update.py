from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
from varieties.apis.serializers import AmenitySerializer

from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def amenity_update(request, pk):
    try:
        amenity = Amenity.objects.get(pk=pk, user=request.user)
        serializer = AmenitySerializer(amenity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': _('Amenity updated successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Amenity.DoesNotExist:
        return Response({'error': _('Amenity object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)