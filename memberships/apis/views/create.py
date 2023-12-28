from memberships.models import Membership, MembershipFeature
from memberships.apis.serializers import MembershipSerializer, UserMembershipSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


from django.utils.translation import gettext as _


@api_view(["POST",])
@permission_classes([permissions.IsAdminUser])
def create_membership(request):

    data = request.data

    if not data:
        return Response({
            "message": _("Please provide data to create your membership")
        }, status=status.HTTP_400_BAD_REQUEST)

    name = data.get("name")
    price = int(data.get('price'))
    features = data.get("features")
    try:
        membership = Membership.objects.create(
            name=name,
            price=price,
        )
        if features:
            for feature in features:
                MembershipFeature.objects.create(
                    feature=feature,
                    membership=membership
                )
        return Response({
            "message": _("The membership was created successfully")
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": _("An error occurred while creating the membership")
        }, status=status.HTTP_400_BAD_REQUEST)
