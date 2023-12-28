from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Size, SubCategory
from varieties.apis.serializers import SizeSerializer

from django.utils.translation import gettext as _

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_size(request):
    try:
        name = request.data.get('name')
        category = request.data.get("category")

        if not name:
            return Response({
                "message": _("Please provide name for the size")
            }, status=status.HTTP_400_BAD_REQUEST)

        if not category:
            return Response({
                "message": _("Please provide category for the size")
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            sub_category = SubCategory.objects.get(name=category)
        except SubCategory.DoesNotExist:
            return Response({
                "message": _("There's no category with this name!")
            }, status=status.HTTP_404_NOT_FOUND)

        is_size_exists = Size.objects.filter(name=name, category=sub_category)

        if is_size_exists:
            return Response({
                "message": _("This size is already exists")
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            Size.objects.create(
                name=name,
                category=sub_category
            )
            return Response({
                "message": _("The size was created successfully!")
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": _("An error occurred while creating the size")
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)