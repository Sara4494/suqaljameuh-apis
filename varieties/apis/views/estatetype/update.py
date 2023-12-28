from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from apartments.models import EstateType
from apartments.apis.serializers import EstateTypeSerializer
 
from django.utils.translation import gettext as _
@api_view(['POST'])
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_estatetype(request, pk):
    try:
        estatetype = EstateType.objects.get(pk=pk)
    except EstateType.DoesNotExist:
        return Response({'error': _('EstateType does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and EstateType.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the EstateType.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EstateTypeSerializer(estatetype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('EstateType updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)