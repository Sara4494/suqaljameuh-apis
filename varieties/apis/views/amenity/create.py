
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Amenity
from varieties.apis.serializers import AmenitySerializer
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def amenity_create(request):
    try:
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Amenity created successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)