 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from apartments.models import EstateType
from apartments.apis.serializers import EstateTypeSerializer
 
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_estatetype(request, pk):
    try:
        estatetype = EstateType.objects.get(pk=pk)
        estatetype.delete()
        return Response({'message': _('EstateType deleted successfully.')}, status=status.HTTP_200_OK)
    except EstateType.DoesNotExist:
        return Response({'error': _('EstateType object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
