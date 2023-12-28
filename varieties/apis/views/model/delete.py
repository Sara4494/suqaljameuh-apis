from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _
 
      
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_model(request, pk):
    try:
        model = Model.objects.get(pk=pk)
        model.delete()
        return Response({'message': _('Model deleted successfully.')}, status=status.HTTP_200_OK)
    except Model.DoesNotExist:
        return Response({'error': _('Model object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)