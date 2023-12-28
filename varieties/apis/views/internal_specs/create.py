from cars.models import InternalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_internal_specs(request):
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
    
    internal_specs_exists = InternalSpecs.objects.filter(name=name).exists()

    if internal_specs_exists:
        return Response({
            "message": "This internal specs already exists"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        InternalSpecs.objects.create(
            name=name
        )
        return Response({
            "message": "The internal specs was created successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"An error occurred while creating the internal specs"
        }, status=status.HTTP_400_BAD_REQUEST)