from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from jobs.models import JobSeeker, ExperienceLevel, ContractType, Grade
from jobs.apis.serializers import JobSeekerSerializer

@api_view(["GET",])
@permission_classes([permissions.AllowAny,])
def get_all(request):
    try:
        ads = JobSeeker.objects.all().order_by('-published_at')
        serializer = JobSeekerSerializer(ads, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting the data of all available ads"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
@permission_classes([permissions.AllowAny,])
def get_offer(request, offer_id):
    try:
        ad = JobSeeker.objects.get(pk=offer_id)
    except JobSeeker.DoesNotExist:
        return Response({
            "message": "couldn't found this ad or may be the publisher deleted it"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = JobSeekerSerializer(ad, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)