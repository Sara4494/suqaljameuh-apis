 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from apartments.models import BuildingAge
from apartments.apis.serializers import BuildingAgeSerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_buildingage(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if BuildingAge.objects.filter(name=name).exists():
                return Response({'error': _('This name is already registered at the BuildingAge.')}, status=status.HTTP_400_BAD_REQUEST)
            serializer = BuildingAgeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': _('BuildingAge created successfully')}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_buildingage(request, pk):
    try:
        buildingage = BuildingAge.objects.get(pk=pk)
    except BuildingAge.DoesNotExist:
        return Response({'error': _('BuildingAge does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and BuildingAge.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the BuildingAge.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BuildingAgeSerializer(buildingage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('BuildingAge updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)