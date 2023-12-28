
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
from varieties.apis.serializers import AmenitySerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def amenity_create(request):
    data = request.data

    name = data.get("name")
    try:
        Amenity.objects.create(
            name = name
        )
        return Response({'message': _('Amenity created successfully.')}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_400_BAD_REQUEST)