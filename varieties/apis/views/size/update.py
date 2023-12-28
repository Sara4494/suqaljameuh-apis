from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size
from varieties.apis.serializers import SizeSerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response({'error': _('Size object not found.')}, status=status.HTTP_404_NOT_FOUND)
    try:
        name = request.data.get('name')
        if name and Size.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the size.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('Size updated successfully'), 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)