from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size
from varieties.apis.serializers import SizeSerializer
def create_size(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if Size.objects.filter(name=name).exists():
                return Response({'error': 'This name is already registered at the size.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = SizeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Size created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

         