from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size
from varieties.apis.serializers import GetSizeSerializer
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_sizes(request):
    try:
        if request.method == 'GET':
            queryset = Size.objects.all()
            serializer = GetSizeSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'Sizes retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
