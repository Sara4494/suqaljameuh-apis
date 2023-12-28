from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Material
from varieties.apis.serializers import MaterialSerializer
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_material(request, pk):
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response({'error': 'Material object not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        material.delete()
        return Response({'success': 'Material deleted successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)