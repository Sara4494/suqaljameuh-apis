
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status ,permissions
from varieties.models import Currency
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_currency(request, pk):
    try:
        currency = Currency.objects.get(pk=pk)
        currency.delete()
        return Response({'message': _('Currency deleted successfully.')}, status=status.HTTP_204_NO_CONTENT)
    except Currency.DoesNotExist:
        return Response({'error': _('Currency object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)