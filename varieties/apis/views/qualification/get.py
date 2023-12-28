
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Qualification
from varieties.apis.serializers import QualificationSerializer

from django.utils.translation import gettext as _


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def qualification_retrieve(request):
    try:
        qualification = Qualification.objects.filter(user=request.user)
        serializer = QualificationSerializer(qualification, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
