from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from jobs.models import JobOffer, ExperienceLevel, ContractType, Grade
from jobs.apis.serializers import JobOfferSerializer

@api_view(["GET",])
@permission_classes([permissions.AllowAny,])
def get_all(request):
    try:
        job_offers = JobOffer.objects.all().order_by('-published_at')
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting the data of all available offers"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
@permission_classes([permissions.AllowAny,])
def get_offer(request, offer_id):
    try:
        job_offer = JobOffer.objects.get(pk=offer_id)
    except JobOffer.DoesNotExist:
        return Response({
            "message": "couldn't found this job offer or may be the publisher deleted it"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = JobOfferSerializer(job_offer, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting the information of the offer"
        }, status=status.HTTP_400_BAD_REQUEST)