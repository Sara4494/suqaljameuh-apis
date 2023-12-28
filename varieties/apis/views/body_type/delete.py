
from cars.models import BodyType
from cars.apis.serializers import BodyTypeSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_body_type(request, body_type_id):
    try:
        body_type = BodyType.objects.get(pk=body_type_id)
    except BodyType.DoesNotExist:
        return Response({
            "message": "Body Type Doesn't exist"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        body_type.delete()
        return Response({
            "message": "The Body Type Deleted Successfully"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the body type"
        }, status=status.HTTP_400_BAD_REQUEST)
