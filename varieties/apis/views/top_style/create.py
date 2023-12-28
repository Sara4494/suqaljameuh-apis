


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import TopStyle
from varieties.apis.serializers import TopStyleSerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_topstyle(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name')
            if TopStyle.objects.filter(name=name).exists():
                return Response({'error': _('This name is already registered at the TopStyle.')}, status=status.HTTP_400_BAD_REQUEST)
            try:
                TopStyle.objects.create(
                    name = name
                )
                return Response({
                    "message": "Topstyle was successfully created!"
                }, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({
                    "message": "an error occurred while creating the topstyle"
                }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)