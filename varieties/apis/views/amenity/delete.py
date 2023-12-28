from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
 
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def amenity_destroy(request, pk):
    try:
        amenity = Amenity.objects.get(pk=pk, user=request.user)
        amenity.delete()
        return Response({'message': _('Amenity deleted successfully.')}, status=status.HTTP_200_OK)
    except Amenity.DoesNotExist:
        return Response({'error': _('Amenity object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)