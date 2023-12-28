from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size
from varieties.apis.serializers import SizeSerializer
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return Response({'error': 'Size object not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        size.delete()
        return Response({'success': 'Size deleted successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
