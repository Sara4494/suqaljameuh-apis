from cars.models import FoulType
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_foul_type(request, foul_type_id):
    data = request.data

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    name = data.get("name")

    try:
        foul_type = FoulType.objects.get(pk=foul_type_id)
    except FoulType.DoesNotExist:
        return Response({
            "message": "The foul type doesn't exists"
        }, status=status.HTTP_400_BAD_REQUEST)


    if name and foul_type.name != name:
        foul_type_exists = FoulType.objects.filter(name=name).exists()
        if foul_type_exists:
            return Response({
                "message": "This foul type already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
        foul_type.name = name
        foul_type.save()
        return Response({
            "message": "Foul Type Updated Successfully"
        }, status=status.HTTP_200_OK)
    return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    