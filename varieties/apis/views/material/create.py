
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Material
from varieties.apis.serializers import MaterialSerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_material(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if Material.objects.filter(name=name).exists():
                return Response({'error': _('This name is already registered at the Material.')}, status=status.HTTP_400_BAD_REQUEST)
            serializer = MaterialSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': _('Material created successfully')}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)