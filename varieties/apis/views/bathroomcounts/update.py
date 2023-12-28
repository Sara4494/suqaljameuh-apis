 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from apartments.models  import BathroomCounts
from apartments.apis.serializers   import BathroomCountsSerializer
from django.utils.translation import gettext as _
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_bathroomcounts(request, pk):
    try:
        bathroomcounts = BathroomCounts.objects.get(pk=pk)
    except BathroomCounts.DoesNotExist:
        return Response({'error': _('BathroomCounts does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and BathroomCounts.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the BathroomCounts.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BathroomCountsSerializer(bathroomcounts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('BathroomCounts updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
