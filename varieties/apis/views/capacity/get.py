from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_capacities(request):
    try:
        if request.method == 'GET':
            queryset = Capacity.objects.all()
            serializer = CapacitySerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'Capacities retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


def get_subcategory_capacities(request, subcategory_id):
    try:
        capacities = Capacity.objects.filter(category__id=subcategory_id)
        serializer = CapacitySerializer(capacities, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting capacities"
        }, status=status.HTTP_400_BAD_REQUEST)