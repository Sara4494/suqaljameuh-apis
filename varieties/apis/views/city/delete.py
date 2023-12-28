from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import City

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def city_destroy(request, pk):
    try:
        city = City.objects.get(pk=pk)
        city.delete()
        return Response({'message': 'City deleted successfully.'}, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response({'error': 'City object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
