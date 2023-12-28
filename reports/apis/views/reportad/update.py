from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 
from rest_framework.response import Response
from rest_framework import status
from reports.models import ReportAd
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render
from reports.apis.serializers import ReportAdSerializer
from rest_framework import decorators
from reports.tasks import *

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def discard_report(request, report_id):
    try:
        report = ReportAd.objects.get(id=report_id)
        report.discard = True
        report.save()
        serializer = ReportAdSerializer(report)
 
        send_user_report_notification.delay(report_id, "The report has been discarded.")

        return Response(serializer.data)
    except ReportAd.DoesNotExist:
        return Response({'error': 'Report not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def flag_report_in_progress(request, report_id):
    try:
        report = ReportAd.objects.get(id=report_id)
        report.in_progress = True
        report.save()
        serializer = ReportAdSerializer(report)

        
        send_user_report_notification.delay(report_id, "The report is now in progress.")

        return Response(serializer.data)
    except ReportAd.DoesNotExist:
        return Response({'error': 'Report not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def flag_report_finalized(request, report_id):
    try:
        report = ReportAd.objects.get(id=report_id)
        report.finalized = True
        report.save()
        serializer = ReportAdSerializer(report)

      
        send_user_report_notification.delay(report_id, "The report has been finalized.")

        return Response(serializer.data)
    except ReportAd.DoesNotExist:
        return Response({'error': 'Report not found.'}, status=status.HTTP_404_NOT_FOUND)
        