from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import SubCategory, Category
from varieties.apis.serializers import SubCategorySerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_subcategories(request):
    try:
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while retrieving the subcategories"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_category_subcategories(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        return Response({
            "message": "Category not found"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        subcategories = SubCategory.objects.filter(
            category=category).order_by("-added_at")
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while retrieving the subcategories"
        }, status=status.HTTP_400_BAD_REQUEST)
