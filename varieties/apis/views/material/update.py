from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Material
from varieties.apis.serializers import MaterialSerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_material(request, pk):
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response({'error': _('Material does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and Material.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the Material.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('Material updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)