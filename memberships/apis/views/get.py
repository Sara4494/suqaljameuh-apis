from memberships.models import Membership, UserMembership
from memberships.apis.serializers import MembershipSerializer, UserMembershipSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.translation import gettext as _


@api_view(["GET"])
def get_memberships(request):
    try:
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": _("An error occurred while retrieving memberships, please try again")
        }, status=status.HTTP_400_BAD_REQUEST)
