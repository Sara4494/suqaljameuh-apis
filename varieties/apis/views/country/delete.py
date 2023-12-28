from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Country
 
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_country(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response({'message': 'Country deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Country.DoesNotExist:
        return Response({'error': 'Country object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
