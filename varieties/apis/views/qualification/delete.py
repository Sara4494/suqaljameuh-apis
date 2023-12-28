
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Qualification
 
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def qualification_destroy(request, pk):
    try:
        qualification = Qualification.objects.get(pk=pk, user=request.user)
        qualification.delete()
        return Response({'success': 'Qualification deleted successfully.'}, status=status.HTTP_200_OK)
    except Qualification.DoesNotExist:
        return Response({'error': 'Qualification object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
