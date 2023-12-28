from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Type
from varieties.apis.serializers import TypeSerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_type(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if Type.objects.filter(name=name).exists():
                return Response({'error': _('This name is already registered at the Type.')}, status=status.HTTP_400_BAD_REQUEST)
            serializer = TypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': _('Type created successfully.')}, status=status.HTTP_201_CREATED)
            return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)