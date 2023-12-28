from rest_framework import generics, mixins
from rest_framework.response import Response
from varieties.apis import serializers
from varieties.models import Category
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status


@api_view(["PUT"])
@permission_classes([permissions.IsAdminUser])
def update_category(request, category_id):
    data = request.data

    if not data:
        return Response({
            "message": "No data to update"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response({
            "message": "category not found"
        }, status=status.HTTP_404_NOT_FOUND)

    name = data.get("name")

    try:
        if name and category.name != name:
            category.name = name
            category.save()
            return Response({
                "message": "The category updated successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "an error occurred while updating the category"
        }, status=status.HTTP_400_BAD_REQUEST)
