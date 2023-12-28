
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Experience
from varieties.apis.serializers import ExperienceSerializer

from django.utils.translation import gettext as _


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def experience_retrieve(request):
    try:
        experience = Experience.objects.filter(user=request.user)
        serializer = ExperienceSerializer(experience, many=True)
        return Response({'message': _('Experience retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
