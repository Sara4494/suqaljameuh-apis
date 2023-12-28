from varieties.models import Mechanism
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def create_mechanism(request):
    data = request.data

    
    if not data:
        return Response({
            "message": "Nothing to create"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("name")
    if not name:
        return Response({
            "message": "Please enter mechanism name"
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        Mechanism.objects.create(
            name = name
        )
        return Response({
            "message": "Mechanism updated successfully"
        }, status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while deleting the mechanism"
        }, status=status.HTTP_400_BAD_REQUEST)