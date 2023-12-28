from cars.models import RegionalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_regional_specs(request, regional_specs_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        regional_specs = RegionalSpecs.objects.get(pk=regional_specs_id)
    except RegionalSpecs.DoesNotExist:
        return Response({
            "message": "The regional specs doesn't exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    if name and regional_specs.name != name:
        regional_specs_exists = RegionalSpecs.objects.filter(name=name).exists()
        if regional_specs_exists:
            return Response({
                "message": "This regional specs already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        regional_specs.name = name
        regional_specs.save()
        return Response({
            "message": "Regional Specs Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)