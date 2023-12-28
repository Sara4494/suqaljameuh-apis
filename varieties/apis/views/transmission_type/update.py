from cars.models import TransmissionType
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_transmission_type(request, transmission_type_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        transmission_type = TransmissionType.objects.get(pk=transmission_type_id)
    except TransmissionType.DoesNotExist:
        return Response({
            "message": "The transmission type doesn't exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    if name and transmission_type.name != name:
        transmission_type_exists = TransmissionType.objects.filter(name=name).exists()
        if transmission_type_exists:
            return Response({
                "message": "This transmission type already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        transmission_type.name = name
        transmission_type.save()
        return Response({
            "message": "Transmission Type Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)