from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from jobs.models import JobOffer, ExperienceLevel, ContractType, Grade
from jobs.apis.serializers import JobOfferSerializer
from users.permissions import UserOwnerOnly, UserActive


@api_view(["GET",])
@permission_classes([UserOwnerOnly, UserActive])
def delete_offer(request, offer_id):
    try:
        job_offer = JobOffer.objects.get(pk=offer_id)
    except JobOffer.DoesNotExist:
        return Response({
            "message": "couldn't found this job offer"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        job_offer.delete()
        return Response({
            "message": "Offer deleted successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while deleting the offer"
        }, status=status.HTTP_400_BAD_REQUEST)
