from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import City
from varieties.apis.serializers import CitySerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def city_create(request):
    try:
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': _('City created successfully.'), 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)