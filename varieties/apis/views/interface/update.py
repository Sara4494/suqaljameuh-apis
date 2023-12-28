from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apartments.models import Interface
from apartments.apis.serializers import InterfaceSerializer
from rest_framework import permissions, status
from django.utils.translation import gettext as _
 
 
 
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_interface(request, pk):
    try:
        interface = Interface.objects.get(pk=pk)
    except Interface.DoesNotExist:
        return Response({'error': _('Interface does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and Interface.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the Interface.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = InterfaceSerializer(interface, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('Interface updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)