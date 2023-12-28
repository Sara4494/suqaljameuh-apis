from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import PaymentMethod

from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def payment_method_destroy(request, pk):
    try:
        payment_method = PaymentMethod.objects.get(pk=pk)
        payment_method.delete()
        return Response({'message': _('Payment method deleted successfully.')}, status=status.HTTP_200_OK)
    except PaymentMethod.DoesNotExist:
        return Response({'error': _('Payment method object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)