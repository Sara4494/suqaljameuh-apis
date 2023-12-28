from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Type
from varieties.apis.serializers import TypeSerializer
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_type(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if Type.objects.filter(name=name).exists():
                return Response({'error': 'This name is already registered at the Type.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = TypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'Type created successfully.'}, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)