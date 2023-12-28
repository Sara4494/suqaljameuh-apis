from varieties.apis import serializers
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from varieties.models import Category
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST",])
@permission_classes([permissions.IsAdminUser])
@parser_classes([FormParser, MultiPartParser])
def create_category(request):
    data = request.data

    if not data:
        return Response({
            "message": "Please enter data to create the category"
        }, status=status.HTTP_400_BAD_REQUEST)

    icon = data.get("icon")
    name = data.get("name")

    if not icon:
        return Response({
            "message": "Please enter an icon to create the category"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not name:
        return Response({
            "message": "Please enter an name to create the category"
        }, status=status.HTTP_400_BAD_REQUEST)

    category_exists = Category.objects.filter(name=name).exists()

    if category_exists:
        return Response({
            "message": "This Category Is Already Registered"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        Category.objects.create(
            name=name,
            icon=icon
        )

        return Response({
            "message": "Category created successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while creating the category"
        }, status=status.HTTP_400_BAD_REQUEST)
