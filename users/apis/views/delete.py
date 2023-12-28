 
from rest_framework.response import Response
from users.models import User
from users.apis.serializers import  UserSerializer
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete(request):
    try:
        if request.method == 'DELETE':
            user = User.objects.get(pk=request.data['id'])
            user.delete()
            return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
