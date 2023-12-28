from cars.models import FoulType
from cars.apis.serializers import FoulTypeSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_foul_type(request, foul_type_id):
    try:
        foul_type = FoulType.objects.get(pk=foul_type_id)
    except FoulType.DoesNotExist:
        return Response({
            "message": "Foul Type Doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        foul_type.delete()
        return Response({
            "message": "The Foul Type Deleted Successfully"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the foul type"
        }, status=status.HTTP_400_BAD_REQUEST)