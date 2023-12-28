 
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from apartments.models import AdditionalFeature
from apartments.apis.serializers import AdditionalFeatureSerializer

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_additional_feature(request, pk):
    try:
        additional_feature = AdditionalFeature.objects.get(pk=pk)
    except AdditionalFeature.DoesNotExist:
        return Response({'error': _('AdditionalFeature does not exist')}, status=status.HTTP_404_NOT_FOUND)

    try:
        name = request.data.get('name')
        if name and AdditionalFeature.objects.filter(name=name).exclude(pk=pk).exists():
            return Response({'error': _('This name is already registered at the AdditionalFeature.')}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AdditionalFeatureSerializer(additional_feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': _('AdditionalFeature updated successfully')}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)