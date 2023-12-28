from cars.models import FoulType
from cars.apis.serializers import FoulTypeSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_foul_types(request):
    try:
        queryset = FoulType.objects.all()
        serializer = FoulTypeSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': 'Foul types retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)