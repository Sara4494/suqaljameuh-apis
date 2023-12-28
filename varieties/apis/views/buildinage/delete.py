from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from apartments.models import BuildingAge
from apartments.apis.serializers import BuildingAgeSerializer
from django.utils.translation import gettext as _
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_buildingage(request, pk):
    try:
        buildingage = BuildingAge.objects.get(pk=pk)
        buildingage.delete()
        return Response({'message': _('BuildingAge deleted successfully.')}, status=status.HTTP_200_OK)
    except BuildingAge.DoesNotExist:
        return Response({'error': _('BuildingAge object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
