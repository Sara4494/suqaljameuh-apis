from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from cars.models import OuterSpecs

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_outer_specs(request, outer_specs_id):
    try:
        outer_specs = OuterSpecs.objects.get(pk=outer_specs_id)
    except OuterSpecs.DoesNotExist:
        return Response({
            "message": "Outer Specs Doesn't exist"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        outer_specs.delete()
        return Response({
            "message": "The Outer Specs Deleted Successfully"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the outer specs"
        }, status=status.HTTP_400_BAD_REQUEST)