from varieties.apis import serializers
from varieties.models import Mechanism
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

@api_view(['GET',])
@permission_classes([permissions.AllowAny])
def get_mechanisms(request):
    try:
        mechanisms = Mechanism.objects.all()
        serializer = serializers.MechanismSerializer(mechanisms, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting all the mechanisms"
        }, status=status.HTTP_400_BAD_REQUEST)