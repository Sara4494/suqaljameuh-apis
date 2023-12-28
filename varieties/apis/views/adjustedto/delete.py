from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from apartments.models import AdjustedTo
from apartments.apis.serializers import AdjustedToSerializer
from django.utils.translation import gettext as _



@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_adjustedto(request, pk):
    try:
        adjustedto = AdjustedTo.objects.get(pk=pk)
        adjustedto.delete()
        return Response({'message': _('AdjustedTo deleted successfully.')}, status=status.HTTP_200_OK)
    except AdjustedTo.DoesNotExist:
        return Response({'error': _('AdjustedTo object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
