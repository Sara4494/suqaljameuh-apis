from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from reports.models import  ReportProblem
from reports.apis.serializers import *
 
from rest_framework.response import Response
from reports.tasks import *
from Ad.models import Ad



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_problems(request):
    content = request.data.get('content')
    if not content:
        return Response({'error': 'problem_content is a required field.'}, status=status.HTTP_400_BAD_REQUEST)
    ad_id = request.data.get('ad_id')
    if not ad_id:
        return Response({'error': 'ad_id is a required field.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ad = Ad.objects.get(id=ad_id)
        report_problem = ReportProblem.objects.create(content=content, reported_by=request.user)
        
        send_admin_problem_notification.delay(report_problem.id, content)
        return Response({'message': 'Problem created successfully.'}, status=status.HTTP_201_CREATED)
    except Ad.DoesNotExist:
        return Response({'error': 'Ad not found.'}, status=status.HTTP_404_NOT_FOUND)
    except:
       return Response({'error': 'Failed to create problem.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
