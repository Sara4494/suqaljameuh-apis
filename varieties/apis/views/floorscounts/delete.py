from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from apartments.models import FloorsCounts
from apartments.apis.serializers import FloorsCountsSerializer
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_floorscounts(request, pk):
    try:
        floorscounts = FloorsCounts.objects.get(pk=pk)
        floorscounts.delete()
        return Response({'message': _('FloorsCounts deleted successfully.')}, status=status.HTTP_200_OK)
    except FloorsCounts.DoesNotExist:
        return Response({'error': _('FloorsCounts object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
