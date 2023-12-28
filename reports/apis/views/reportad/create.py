from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core import exceptions
from reports.apis.serializers import *
from reports.models import ReportAd
from Ad.models import Ad
from reports.tasks import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_report(request):
    try:
        content = request.data.get('content')
        ad_id = request.data.get('ad')
        if not content or not ad_id:
            return Response({'error': 'Both content and ad are required fields.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ad = Ad.objects.get(pk=ad_id)
        except exceptions.ObjectDoesNotExist:
            return Response({'error': 'Ad not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            if request.user == ad.user:
                return Response({
                    "message": "You can't report your ad"
                }, status=status.HTTP_400_BAD_REQUEST)
            report_ad = ReportAd.objects.create(
                content=content, ad=ad, reported_by=request.user)
            send_admin_report_notification.delay(
                report_id=report_ad.id, content=content)
            return Response({
                "message": "Thanks for sending a report, we have received it and we are going to inspect it"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': "an error occurred while creating your report"
            }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'message': "an error occurred while creating your report please try again"}, status=status.HTTP_400_BAD_REQUEST)
