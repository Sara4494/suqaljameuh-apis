from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_rent_periods(request):
    try:
        if request.method == 'GET':
            queryset = RentPeriod.objects.all()
            serializer = RentPeriodSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'RentPeriods retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
