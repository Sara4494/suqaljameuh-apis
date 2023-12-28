from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_kilometer(request, pk):
    try:
        kilometer = KiloMeter.objects.get(pk=pk)
    except KiloMeter.DoesNotExist:
        return Response({'error': _('KiloMeter does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and KiloMeter.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the KiloMeter.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = KiloMeterSerializer(kilometer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('KiloMeter updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)