from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from varieties.models import Currency
from varieties.apis.serializers import CurrencySerializer
@api_view(['GET'])
def currency_detail(request, pk):
    try:
        currency = Currency.objects.get(pk=pk)
        serializer = CurrencySerializer(currency)
        return Response({'message': 'Currency retrieved successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
    except Currency.DoesNotExist:
        return Response({'error': 'Currency object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
