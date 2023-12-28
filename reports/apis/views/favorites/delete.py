from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from reports.models import Favorites
from reports.apis.serializers import *
from users.permissions import UserOwnerOnly, UserActive


@api_view(['DELETE'])
@permission_classes([UserActive, UserOwnerOnly])
def delete_favorite(request, favorite_id):
    try:
        favorite = Favorites.objects.get(id=favorite_id, user=request.user)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Favorites.DoesNotExist:
        return Response({'message': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
