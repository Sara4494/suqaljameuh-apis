from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import City

from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def city_destroy(request, pk):
    try:
        city = City.objects.get(pk=pk)
        city.delete()
        return Response({'message': _('City deleted successfully.')}, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response({'error': _('City object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)