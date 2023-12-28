from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from apartments.models import NearLocation
from apartments.apis.serializers import NearLocationSerializer
from rest_framework import permissions, status
from django.utils.translation import gettext as _


@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_nearlocation(request, pk):
    try:
        nearlocation = NearLocation.objects.get(pk=pk)
        nearlocation.delete()
        return Response({'message': _('NearLocation deleted successfully.')}, status=status.HTTP_200_OK)
    except NearLocation.DoesNotExist:
        return Response({'error': _('NearLocation object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
