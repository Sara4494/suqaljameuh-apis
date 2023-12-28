from reports.models import ReportComment
from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from reports.apis.serializers import ReportCommentSerializer


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAuthenticated])
def Update_Comments_Reports(request, report_id):
    reported_comment = get_object_or_404(ReportComment, id=report_id)
    try:

        if request.user != reported_comment.report_by:
            return Response({"message": "you don't have the permissions to update"}, status=status.HTTP_400_BAD_REQUEST)

        content = request.data.get('content', None)

        if content is None:
            return Response({'message': "Please insert 'content' field"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'report_by': request.user.id,
            'comment': reported_comment.comment.id,
            'content': content,
        }

        serializer = ReportCommentSerializer(reported_comment, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        return Response({'message': f'an error accoured : {error}'}, status=status.HTTP_400_BAD_REQUEST)
