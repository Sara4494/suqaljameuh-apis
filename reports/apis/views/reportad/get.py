from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from reports.models import ReportAd
from reports.apis.serializers import *
from rest_framework import status
from Ad.models import Ad


@api_view(['GET'])
@permission_classes([IsAdminUser])
def retrieve_reports(request):
    try:
        reports = ReportAd.objects.filter(discard=False)
        serializer = ReportAdSerializer(reports, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def retrieve_single_report(request, report_id):
    try:
        report = ReportAd.objects.get(id=report_id, discard=False)
        serializer = ReportAdSerializer(report)
        try:
            ads_count = Ad.objects.filter(user__id=request.user.id).count()
        except Exception as e:
            return Response({
                "message": "an error occurred while calculating user's ads"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "data": serializer.data,
            "ads_count": ads_count
        }, status=status.HTTP_200_OK)
    except ReportAd.DoesNotExist:
        return Response({'message': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
