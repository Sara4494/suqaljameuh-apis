from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import TopStyle
from django.utils.translation import gettext as _

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_topstyle(request, pk):
    try:
        topstyle = TopStyle.objects.get(pk=pk)
    except TopStyle.DoesNotExist:
        return Response({'error': _('TopStyle object not found.')}, status=status.HTTP_404_NOT_FOUND)
    try:
        topstyle.delete()
        return Response({'success': _('TopStyle deleted successfully.')}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)