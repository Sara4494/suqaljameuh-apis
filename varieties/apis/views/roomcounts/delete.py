from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from apartments.models import RoomCounts
from apartments.apis.serializers import RoomCountsSerializer
from rest_framework import permissions, status
from django.utils.translation import gettext as _
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_roomcounts(request, pk):
    try:
        roomcounts = RoomCounts.objects.get(pk=pk)
        roomcounts.delete()
        return Response({'message': _('RoomCounts deleted successfully.')}, status=status.HTTP_200_OK)
    except RoomCounts.DoesNotExist:
        return Response({'error': _('RoomCounts object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 