from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from jobs.models import JobSeeker, ExperienceLevel, ContractType, Grade
from users.permissions import UserOwnerOnly, UserActive


@api_view(["GET",])
@permission_classes([UserActive, UserOwnerOnly])
def delete_seeker(request, ad_id):
    try:
        ad = JobSeeker.objects.get(pk=ad_id)
    except JobSeeker.DoesNotExist:
        return Response({
            "message": "couldn't found this ad"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        ad.delete()
        return Response({
            "message": "Ad deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while deleting the ad"
        }, status=status.HTTP_400_BAD_REQUEST)
