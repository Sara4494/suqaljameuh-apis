from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import PaymentMethod
from varieties.apis.serializers import PaymentMethodSerializer

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def payment_method_update(request, pk):
    try:
        payment_method = PaymentMethod.objects.get(pk=pk)
        serializer = PaymentMethodSerializer(payment_method, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Payment method updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except PaymentMethod.DoesNotExist:
        return Response({'error': 'Payment method object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
