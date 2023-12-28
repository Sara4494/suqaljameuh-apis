from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size 
from varieties.apis.serializers import SizeSerializer
from django.utils.translation import gettext as _
 
from varieties.apis.serializers import SizeSerializer

 
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_sizes(request):
    try:
        if request.method == 'GET':
            queryset = Size.objects.all()
 
            serializer = SizeSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': _('Sizes retrieved successfully.')}, status=status.HTTP_200_OK)
  
 
        else:
            return Response({'error': _('Invalid request method.')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

def get_subcategory_sizes(request, subcategory_id):
    try:
        sizes = Size.objects.filter(category__id=subcategory_id)
        serializer = SizeSerializer(sizes, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting sizes"
        }, status=status.HTTP_400_BAD_REQUEST)