from cars.models import RegionalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_regional_specs(request):
    data = request.data

    if not data:
        return Response({
            "message": "Please enter the data"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("name")

    if not name:
        return Response({
            "message": "Please enter the name"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    regional_specs_exists = RegionalSpecs.objects.filter(name=name).exists()

    if regional_specs_exists:
        return Response({
            "message": "This regional specs already exists"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        RegionalSpecs.objects.create(
            name=name
        )
        return Response({
            "message": "The regional specs was created successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"An error occurred while creating the regional specs"
        }, status=status.HTTP_400_BAD_REQUEST)