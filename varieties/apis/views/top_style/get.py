from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import TopStyle
 
from varieties.apis.serializers import TopStyleSerializer
from django.utils.translation import gettext as _

 

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_topstyles(request):
    try:
        queryset = TopStyle.objects.all()
        serializer = TopStyleSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': _('TopStyles retrieved successfully.')}, status=status.HTTP_200_OK)
 
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)