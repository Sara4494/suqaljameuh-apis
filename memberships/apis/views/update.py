from memberships.models import Membership, MembershipFeature
from memberships.apis.serializers import MembershipSerializer, UserMembershipSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.utils.translation import gettext as _


@api_view(["PUT",])
@permission_classes([permissions.IsAdminUser])
def update_membership(request, membership_id):
    data = request.data

    if not data:
        return Response({
            "message": _("No data to update the membership")
        }, status=status.HTTP_400_BAD_REQUEST)
    name = data.get("name")
    price = data.get("price")
    features = data.get("features")

    try:
        membership = Membership.objects.get(pk=membership_id)
    except Membership.DoesNotExist:
        return Response({
            "message": _("There's no membership with this name")
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        is_updated = False
        if name and membership.name != name:
            membership.name = name
            is_updated = True

        if price and membership.price != price:
            membership.price = price
            is_updated = True

        if features:
            feature_list = []
            for feature in features:
                feature_model, created = MembershipFeature.objects.get_or_create(
                    feature=feature,
                    membership=membership
                )
                print(feature_model)
                feature_list.append(feature_model)
            membership.membership_features.set(feature_list)
            is_updated = True

        if is_updated == True:
            membership.save()
            return Response({
                "message": _("the membership updated successfully")
            }, status=status.HTTP_200_OK)
        return Response({
            "message": _("nothing was updated")
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": _(f"an error occurred while updating the membership! please try again {e}")
        }, status=status.HTTP_400_BAD_REQUEST)
