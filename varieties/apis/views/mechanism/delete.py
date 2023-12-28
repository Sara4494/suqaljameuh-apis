from varieties.apis import serializers
from varieties.models import Mechanism
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

@api_view(['GET',])
@permission_classes([permissions.AllowAny])
def delete_mechanism(request, mechanism_id):
    try:
        mechanism = Mechanism.objects.get(pk=mechanism_id)
    except Mechanism.DoesNotExist:
        return Response({
            "message": "Couldn't find this mechanism"
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        mechanism.delete()
        return Response({
            "message": "Mechanism deleted successfully"
        }, status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while deleting the mechanism"
        }, status=status.HTTP_400_BAD_REQUEST)