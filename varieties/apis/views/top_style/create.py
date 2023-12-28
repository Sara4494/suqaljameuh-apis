


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import TopStyle
from varieties.apis.serializers import TopStyleSerializer
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_topstyle(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if TopStyle.objects.filter(name=name).exists():
                return Response({'error': 'This name is already registered at the TopStyle.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = TopStyleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'TopStyle created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
