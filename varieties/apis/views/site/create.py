from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_site(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if Site.objects.filter(name=name).exists():
                return Response({'error': _('This name is already registered at the Site.')}, status=status.HTTP_400_BAD_REQUEST)
            serializer = SiteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': _('Site created successfully')}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_sites(request):
    try:
        if request.method == 'GET':
            queryset = Site.objects.all()
            serializer = SiteSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'Sites retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)