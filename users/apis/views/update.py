from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from users.models import User
from users.apis.serializers import  UserSerializer
from rest_framework import status ,permissions

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update(request):
    try:
        if request.method == 'PUT':
            user = User.objects.get(pk=request.data['id'])
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'User updated successfully.'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)