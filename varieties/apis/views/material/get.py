
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Material
from varieties.apis.serializers import *

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_materials(request):
    try:
        if request.method == 'GET':
            queryset = Material.objects.all()
            serializer = MaterialSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'Materials retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)