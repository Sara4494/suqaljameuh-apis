from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.core import exceptions
from Ad.models import Ad
from users.permissions import UserOwnerOnly


@api_view(["DELETE"])
@permission_classes([UserOwnerOnly])
def delete_ad(request, ad_id):
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "This Ad Doesn't Exists Or Maybe The Publisher Deleted It"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        ad.delete()
        return Response({
            "message": "the ad was deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while deleting the ad"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def delete_ads(request):
    try:
        ads = Ad.objects.all()
    except Exception as e:
        return Response({
            "message": "This Ad Doesn't Exists Or Maybe The Publisher Deleted It"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        for ad in ads:
            ad.delete()
        return Response({
            "message": "the ad was deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while deleting the ad"
        }, status=status.HTTP_400_BAD_REQUEST)
