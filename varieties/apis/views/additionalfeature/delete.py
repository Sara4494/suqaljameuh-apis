 
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from apartments.models import AdditionalFeature
from apartments.apis.serializers import AdditionalFeatureSerializer

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_additional_feature(request, pk):
    try:
        additional_feature = AdditionalFeature.objects.get(pk=pk)
        additional_feature.delete()
        return Response({'message': _('AdditionalFeature deleted successfully.')}, status=status.HTTP_200_OK)
    except AdditionalFeature.DoesNotExist:
        return Response({'error': _('AdditionalFeature object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
