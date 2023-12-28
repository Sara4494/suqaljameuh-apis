from comments.models import AdComment
from comments.apis.serializers import AdCommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.permissions import UserOwnerOnly, UserActive


@api_view(["DELETE"])
@permission_classes([UserActive, UserOwnerOnly])
def delete_comment(request, comment_id):
    try:
        comment = AdComment.objects.get(pk=comment_id)
    except AdComment.DoesNotExist:
        return Response({
            "message": "Comment not found"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        comment.delete()
        return Response({
            "message": "Comment Deleted Successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while deleting the comment"
        }, status=status.HTTP_400_BAD_REQUEST)
