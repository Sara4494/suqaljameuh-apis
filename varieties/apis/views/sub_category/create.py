

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import SubCategory
from varieties.apis.serializers import SubCategorySerializer
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_subcategory(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            category_id = request.data.get('category_id')
            if SubCategory.objects.filter(name=name, category_id=category_id).exists():
                return Response({'error': 'This name is already registered at the SubCategory.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = SubCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Subcategory created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
