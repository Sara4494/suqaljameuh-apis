
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Qualification
from varieties.apis.serializers import QualificationSerializer
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def qualification_create(request):
    try:
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'data': serializer.data, 'message': 'Qualification created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors, 'message': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e), 'message': 'Internal server error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
