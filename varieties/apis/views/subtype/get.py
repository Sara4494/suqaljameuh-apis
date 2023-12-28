from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_subtypes(request):
    try:
        if request.method == 'GET':
            queryset = SubType.objects.all()
            serializer = SubTypeSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'SubTypes retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_type_subtypes(request, type_id):
    try:
        queryset = SubType.objects.filter(type__id=type_id)
        serializer = SubTypeSerializer(queryset, many=True)
        return Response({'data': serializer.data, 'message': 'SubTypes retrieved successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
