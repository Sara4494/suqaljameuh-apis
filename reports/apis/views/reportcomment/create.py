from comments.models import AdComment
from ....models import ReportComment
from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def Create_Comment_Report(request, comment_id):
    comment = get_object_or_404(AdComment, id=comment_id)
    try:

        if request.user == comment.user:
            return Response({'message': "you can't report your comment "}, status=status.HTTP_400_BAD_REQUEST)

        content = request.data.get('content', None)

        if content is None:
            return Response({'message': "Please insert 'content' field"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ReportComment.objects.create(
                content=content,
                comment=comment,
                report_by=request.user
            )
            return Response({
                "message": "Thanks for sending us a report "
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': f'an error occurred please try again'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({'message': f'an error occurred : {error}'}, status=status.HTTP_400_BAD_REQUEST)
