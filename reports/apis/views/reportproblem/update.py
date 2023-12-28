from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from reports.models import  ReportProblem
from reports.apis.serializers import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from reports.tasks import *
  
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def discard_problem(request, problem_id):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        problem.discard = True
        problem.save()
        serializer = ReportProblemSerializer(problem)
      
        send_user_problemt_notification.delay(problem_id, "The problem has been discarded.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ReportProblem.DoesNotExist:
        return Response({'error': 'Problem report not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def flag_problem_in_progress(request, problem_id):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        problem.in_progress = True
        problem.save()
        serializer = ReportProblemSerializer(problem)
         
        send_user_problemt_notification.delay(problem_id, "The problem has been progress.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ReportProblem.DoesNotExist:
        return Response({'error': 'Problem report not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def flag_problem_finalized(request, problem_id):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        problem.finalized = True
        problem.save()
        serializer = ReportProblemSerializer(problem)
       
        send_user_problemt_notification.delay(problem_id, "The problem has been finalized.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ReportProblem.DoesNotExist:
        return Response({'error': 'Problem report not found.'}, status=status.HTTP_404_NOT_FOUND)