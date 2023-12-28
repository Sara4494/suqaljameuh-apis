
from cars.models import BodyType
from cars.apis.serializers import BodyTypeSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_body_type(request, body_type_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        body_type = BodyType.objects.get(pk=body_type_id)
    except BodyType.DoesNotExist:
        return Response({
            "message": "The body type doesn't exist"
        }, status=status.HTTP_400_BAD_REQUEST)

    if name and body_type.name != name:
        body_type_exists = BodyType.objects.filter(name=name).exists()
        if body_type_exists:
            return Response({
                "message": "This body type already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        body_type.name = name
        body_type.save()
        return Response({
            "message": "Body Type Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)