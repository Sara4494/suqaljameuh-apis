

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import SubCategory, Category
from varieties.apis.serializers import SubCategorySerializer
from django.utils.translation import gettext as _


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_subcategory(request):
    data = request.data

    name = data.get("name")
    category = data.get("category")

    if not category:
        return Response({
            "message": "Please enter an category to create the subcategory"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not name:
        return Response({
            "message": "Please enter an name to create the subcategory"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        category_model = Category.objects.get(
            name=category
        )
    except Category.DoesNotExist:
        return Response({'error': _('Category Not Found')}, status=status.HTTP_404_NOT_FOUND)

    category_exists = SubCategory.objects.filter(
        name=name, category=category_model).exists()

    if category_exists:
        return Response({
            "message": "This Subcategory Is Already Registered"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        SubCategory.objects.create(
            category=category_model,
            name=name
        )
        return Response({'error': _('Subcategory created successfully')}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': _('an error occurred while creating the subcategory')}, status=status.HTTP_400_BAD_REQUEST)
