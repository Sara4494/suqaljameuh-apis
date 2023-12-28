from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Experience
from varieties.apis.serializers import ExperienceSerializer

  
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def experience_destroy(request, pk):
    try:
        experience = Experience.objects.get(pk=pk, user=request.user)
        experience.delete()
        return Response({'message': _('Experience deleted successfully.')}, status=status.HTTP_200_OK)
    except Experience.DoesNotExist:
        return Response({'error': _('Experience object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)