

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import SubCategory
from varieties.apis.serializers import SubCategorySerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_subcategory(request, pk):
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response({'error': _('SubCategory object not found.')}, status=status.HTTP_404_NOT_FOUND)
    try:
        name = request.data.get('name')
        category_id = request.data.get('category_id')
        if name and category_id and SubCategory.objects.filter(name=name, category_id=category_id).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the SubCategory.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('Subcategory updated successfully.')}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)