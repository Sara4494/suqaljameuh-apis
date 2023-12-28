from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from apartments.models import AdjustedTo
from apartments.apis.serializers import AdjustedToSerializer
from django.utils.translation import gettext as _



@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_adjustedto(request):
    try:
        if request.method == 'GET':
            queryset = AdjustedTo.objects.all()
            serializer = AdjustedToSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'AdjustedTo retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
