from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Type
from varieties.apis.serializers import TypeSerializer
@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_type(request, pk):
    try:
        type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
        return Response({'error': 'Type object not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        type.delete()
        return Response({'message': 'Type deleted successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
