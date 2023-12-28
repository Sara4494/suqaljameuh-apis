from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_rent_period(request, pk):
    try:
        rentperiod = RentPeriod.objects.get(pk=pk)
        rentperiod.delete()
        return Response({'message': _('RentPeriod deleted successfully.')}, status=status.HTTP_200_OK)
    except RentPeriod.DoesNotExist:
        return Response({'error': _('RentPeriod object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)