from cars.models import InternalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_internal_specs(request, internal_specs_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        internal_specs = InternalSpecs.objects.get(pk=internal_specs_id)
    except InternalSpecs.DoesNotExist:
        return Response({
            "message": "The internal specs doesn't exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    if name and internal_specs.name != name:
        internal_specs_exists = InternalSpecs.objects.filter(name=name).exists()
        if internal_specs_exists:
            return Response({
                "message": "This internal specs already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        internal_specs.name = name
        internal_specs.save()
        return Response({
            "message": "Internal Specs Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)