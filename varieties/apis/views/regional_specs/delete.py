from cars.models import RegionalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_regional_specs(request, regional_specs_id):
    try:
        regional_specs = RegionalSpecs.objects.get(pk=regional_specs_id)
    except RegionalSpecs.DoesNotExist:
        return Response({
            "message": "Regional Specs Doesn't exist"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        regional_specs.delete()
        return Response({
            "message": "The Regional Specs Deleted Successfully"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the regional specs"
        }, status=status.HTTP_400_BAD_REQUEST)