from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from apartments.models import EstateType
from apartments.apis.serializers import EstateTypeSerializer
 
from django.utils.translation import gettext as _
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_estatetype(request):
    try:
        if request.method == 'GET':
            queryset = EstateType.objects.all()
            serializer = EstateTypeSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'EstateType retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
