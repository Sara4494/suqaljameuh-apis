from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from cars.models import OuterSpecs
 

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_outer_specs(request, outer_specs_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        outer_specs = OuterSpecs.objects.get(pk=outer_specs_id)
    except OuterSpecs.DoesNotExist:
        return Response({
            "message": "The outer specs doesn't exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    if name and outer_specs.name != name:
        outer_specs_exists = OuterSpecs.objects.filter(name=name).exists()
        if outer_specs_exists:
            return Response({
                "message": "This outer specs already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        outer_specs.name = name
        outer_specs.save()
        return Response({
            "message": "Outer Specs Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)

