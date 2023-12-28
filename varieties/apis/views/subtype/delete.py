from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
 
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_subtype(request, pk):
    try:
        subtype = SubType.objects.get(pk=pk)
        subtype.delete()
        return Response({'message': _('SubType deleted successfully.')}, status=status.HTTP_200_OK)
    except SubType.DoesNotExist:
        return Response({'error': _('SubType object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)