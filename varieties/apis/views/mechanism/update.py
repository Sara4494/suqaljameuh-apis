from varieties.apis import serializers
from varieties.models import Mechanism
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

@api_view(['GET',])
@permission_classes([permissions.AllowAny])
def update_mechanism(request, mechanism_id):
    data = request.data

    
    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("name")
    try:
        mechanism = Mechanism.objects.get(pk=mechanism_id)
    except Mechanism.DoesNotExist:
        return Response({
            "message": "Couldn't find this mechanism"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if mechanism.name != name:
            mechanism.name = name
            mechanism.save()
            return Response({
                "message": "Mechanism updated successfully"
            }, status.HTTP_200_OK)
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": f"an error occurred while deleting the mechanism"
        }, status=status.HTTP_400_BAD_REQUEST)