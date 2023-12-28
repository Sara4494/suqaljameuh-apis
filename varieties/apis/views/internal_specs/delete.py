
from cars.models import InternalSpecs
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_internal_specs(request, internal_specs_id):
    try:
        internal_specs = InternalSpecs.objects.get(pk=internal_specs_id)
    except InternalSpecs.DoesNotExist:
        return Response({
            "message": "Internal Specs Doesn't exist"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        internal_specs.delete()
        return Response({
            "message": "The Internal Specs Deleted Successfully"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the internal specs"
        }, status=status.HTTP_400_BAD_REQUEST)
