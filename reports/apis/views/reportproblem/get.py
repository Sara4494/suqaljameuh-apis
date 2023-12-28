from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from reports.models import  ReportProblem
from reports.apis.serializers import *



@api_view(['GET'])
@permission_classes([IsAdminUser])
def retrieve_problems(request):
    try:
        problems = ReportProblem.objects.all()
        serializer = ReportProblemSerializer(problems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def retrieve_single_problem(request, problem_id):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        serializer = ReportProblemSerializer(problem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ReportProblem.DoesNotExist:
        return Response({'message': 'Problem not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': 'An error occurred', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
