from varieties.models import *
from varieties.apis.serializers import *
from rest_framework.response import Response
from rest_framework import permissions, status
 
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _
@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_capacity(request):
    try:
        name = request.data.get('name')
        category_id = request.data.get('category_id')
        try:
            category = SubCategory.objects.get(pk=category_id)
        except SubCategory.DoesNotExist:
            return Response({
                "message": _("couldn't find this category")
            }, status=status.HTTP_404_NOT_FOUND)
        if Capacity.objects.filter(name=name, category=category).exists():
            return Response({'error': _('This name is already registered at the Capacity.')}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Capacity.objects.create(
                name = name,
                category = category
            )
            return Response({'error': _('Capacity Created Successfully')}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "an error occurred while creating the capacity"
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
