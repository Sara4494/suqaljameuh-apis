from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_models(request):
    try:
        queryset = Model.objects.all()
        serializer = ModelSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': 'Models retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_subcategory_models(request, subcategory_id):
    try:
        models = Model.objects.filter(category__id=subcategory_id)
        serializer = serializers.ModelSerializer(models, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting models"
        }, status=status.HTTP_400_BAD_REQUEST)