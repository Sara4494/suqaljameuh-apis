from rest_framework.response import Response
from varieties.apis.serializers import ReportAdSerializer
from varieties.models import ReportAd
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, permission_classes
 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_reports(request):
    serializer = ReportAdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(reported_by=request.user)
        # Send real-time notification to ADMINS
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)