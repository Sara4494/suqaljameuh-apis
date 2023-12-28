
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from cars.models import OuterSpecs
from cars.apis.serializers import OuterSpecsSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_outer_specs(request):
    try:
        queryset = OuterSpecs.objects.all()
        serializer = OuterSpecsSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': 'Outer Specs retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
