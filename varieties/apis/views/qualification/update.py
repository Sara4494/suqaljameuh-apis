
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Qualification
from varieties.apis.serializers import QualificationSerializer

from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def qualification_update(request, pk):
    try:
        qualification = Qualification.objects.get(pk=pk, user=request.user)
        serializer = QualificationSerializer(qualification, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': _('Qualification updated successfully.')}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Qualification.DoesNotExist:
        return Response({'error': _('Qualification object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)