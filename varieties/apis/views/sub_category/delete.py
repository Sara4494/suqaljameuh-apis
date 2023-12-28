

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import SubCategory
from varieties.apis.serializers import SubCategorySerializer
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_subcategory(request, pk):
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response({'error': 'SubCategory object not found.'}, status=status.HTTP_404_NOT_FOUND)
    try:
        subcategory.delete()
        return Response({'success': 'Subcategory deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
