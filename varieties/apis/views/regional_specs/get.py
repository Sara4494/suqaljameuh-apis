from cars.models import RegionalSpecs
from cars.apis.serializers import RegionalSpecsSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_regional_specs(request):
    try:
        queryset = RegionalSpecs.objects.all()
        serializer = RegionalSpecsSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': 'Internal Specifications retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)