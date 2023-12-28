from cars.models import TransmissionType
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_transmission_type(request, transmission_type_id):
    try:
        transmission_type = TransmissionType.objects.get(pk=transmission_type_id)
    except TransmissionType.DoesNotExist:
        return Response({
            "message": "Transmission Type Doesn't exist"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        transmission_type.delete()
        return Response({
            "message": "The Transmission Type Deleted Successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the transmission type"
        }, status=status.HTTP_400_BAD_REQUEST)