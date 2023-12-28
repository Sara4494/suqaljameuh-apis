
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Qualification
from varieties.apis.serializers import QualificationSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def qualification_retrieve(request, pk):
    try:
        qualification = Qualification.objects.get(pk=pk, user=request.user)
        serializer = QualificationSerializer(qualification)
        return Response(serializer.data)
    except Qualification.DoesNotExist:
        return Response({'error': 'Qualification object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
