from rest_framework import generics, mixins
from rest_framework.response import Response
from varieties.apis import serializers
from varieties.models import Category
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


@api_view(["DELETE"])
@permission_classes([permissions.IsAdminUser])
def delete_category(request, category_id):

    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response({
            "message": "category not found"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        category.delete()
        return Response({
            "message": "The category was deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while updating the category"
        }, status=status.HTTP_400_BAD_REQUEST)
