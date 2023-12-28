from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from apartments.models import FloorsCounts
from apartments.apis.serializers import FloorsCountsSerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_floorscounts(request, pk):
    try:
        floorscounts = FloorsCounts.objects.get(pk=pk)
    except FloorsCounts.DoesNotExist:
        return Response({'error': _('FloorsCounts does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and FloorsCounts.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the FloorsCounts.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FloorsCountsSerializer(floorscounts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('FloorsCounts updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)