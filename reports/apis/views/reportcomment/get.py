from reports.models import ReportComment
from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from reports.apis.serializers import ReportCommentSerializer
from Ad.models import Ad


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def Get_Comments_Reports(request):
    try:
        queryset = ReportComment.objects.filter(discard=False)
        serializer = ReportCommentSerializer(queryset, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message': f'an error accoured : {error}'}, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def comment_report(request, report_id):
    try:
        report = ReportComment.objects.get(id=report_id, discard=False)
        serializer = ReportCommentSerializer(report, many=False)
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
    except ReportComment.DoesNotExist:
        return Response({'message': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)