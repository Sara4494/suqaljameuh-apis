from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Type
from varieties.apis.serializers import TypeSerializer
from django.utils.translation import gettext as _

@api_view(['PUT'])
def update_type(request, pk):
    try:
        type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
        return Response({'error': _('Type object not found.')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and Type.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the Type.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TypeSerializer(type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': _('Type updated successfully.')}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)