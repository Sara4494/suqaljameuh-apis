from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from varieties.models import Currency
from varieties.apis.serializers import CurrencySerializer
from django.utils.translation import gettext as _

@api_view(['GET'])
def get_currencies(request):
    try:
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        return Response({'message': _('Currencies retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)