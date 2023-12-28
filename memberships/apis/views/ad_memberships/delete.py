from memberships.models import AdMembership
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from django.utils.translation import gettext as _
@api_view(["DELETE",])
@permission_classes([permissions.IsAdminUser])
def delete_membership(request, name):
    try:
        membership = AdMembership.objects.get(name=name)
    except AdMembership.DoesNotExist:
        return Response({
            "message": _("There's no membership with this name")
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        membership.delete()
        return Response({
            "message":-_("membership was deleted successfully!")
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": _(f"an error occurred while deleting the membership! please try again")
        }, status=status.HTTP_400_BAD_REQUEST)
