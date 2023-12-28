
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import PaymentMethod
from varieties.apis.serializers import PaymentMethodSerializer


from django.utils.translation import gettext as _

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def payment_method_retrieve(request, pk):
    try:
        payment_method = PaymentMethod.objects.get(pk=pk)
        serializer = PaymentMethodSerializer(payment_method)
        return Response({'message': _('Payment method retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except PaymentMethod.DoesNotExist:
        return Response({'error': _('Payment method object not found.')}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def payment_methods_retrieve(request):
    try:
        payment_methods = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payment_methods, many=True)
        return Response({'message': _('Payment methods retrieved successfully.'), 'data': serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)