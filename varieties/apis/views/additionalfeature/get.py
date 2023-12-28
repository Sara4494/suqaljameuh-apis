from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from apartments.models import AdditionalFeature
from apartments.apis.serializers import AdditionalFeatureSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_additional_features(request):
    try:
        if request.method == 'GET':
            queryset = AdditionalFeature.objects.all()
            serializer = AdditionalFeatureSerializer(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'AdditionalFeatures retrieved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 