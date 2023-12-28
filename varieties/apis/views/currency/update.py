
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status,permissions
from varieties.models import Currency
from varieties.apis.serializers import CurrencySerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_currency(request, pk):
    try:
        currency = Currency.objects.get(pk=pk)
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': _('Currency updated successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Currency.DoesNotExist:
        return Response({'error': _('Currency object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    