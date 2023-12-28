from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from users.models import User
from users.apis.serializers import  UserSerializer
from rest_framework import status,permissions
from rest_framework import status 
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def get(request):
    try:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'data': serializer.data, 'message': 'Users retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
