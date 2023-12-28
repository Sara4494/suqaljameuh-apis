
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Type
from varieties.apis.serializers import GetTypeSerializer
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_types(request):
    try:
        if request.method == 'GET':
            queryset = Type.objects.all()
            serializer = GetTypeSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'Types retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
