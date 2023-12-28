
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from cars.models import OuterSpecs
 
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_outer_specs(request):
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
    
    outer_specs_exists = OuterSpecs.objects.filter(name=name).exists()

    if outer_specs_exists:
        return Response({
            "message": "This outer specs already exists"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        OuterSpecs.objects.create(
            name=name
        )
        return Response({
            "message": "The outer specs was created successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"An error occurred while creating the outer specs"
        }, status=status.HTTP_400_BAD_REQUEST)