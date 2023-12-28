from reports.models import ReportComment
from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAdminUser])
def Delete_Comments_Reports(request, report_id):

    comment_report = get_object_or_404(ReportComment, id=report_id)
    try:
        comment_report.delete()
        return Response({'message': 'comment has been deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message': f'an error accoured : {error}'}, status=status.HTTP_400_BAD_REQUEST)
