from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import TopStyle
from varieties.apis.serializers import TopStyleSerializer
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_topstyle(request, pk):
    try:
        topstyle = TopStyle.objects.get(pk=pk)
    except TopStyle.DoesNotExist:
        return Response({'error': 'TopStyle object not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and TopStyle.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': 'This name is already registered at the TopStyle.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TopStyleSerializer(topstyle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'message': 'TopStyle updated successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
