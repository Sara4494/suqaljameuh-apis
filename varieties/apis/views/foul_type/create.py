from cars.models import FoulType
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_foul_type(request):
    data = request.data

    if not data:
        return Response({
            "message": "Please enter the data"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("name")

    if not name:
        return Response({
            "message": "Please enter the name"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    foul_type_exists = FoulType.objects.filter(name=name).exists()

    if foul_type_exists:
        return Response({
            "message": "This foul type already exists"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        FoulType.objects.create(
            name = name
        )
        return Response({
            "message": "The foul type was created successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while creating the foul type"
        }, status=status.HTTP_400_BAD_REQUEST)