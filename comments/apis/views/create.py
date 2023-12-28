from comments.models import AdComment
from comments.apis.serializers import AdCommentSerializer
from Ad.models import Ad
from users.permissions import UserActive
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.core import exceptions
from comments.tasks import send_comment_notification


@api_view(["POST"])
@permission_classes([UserActive])
def add_comment(request, ad_id):
    data = request.data
    user = request.user

    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "couldn't find the ad"
        }, status=status.HTTP_404_NOT_FOUND)

    if not data:
        return Response({
            "message": "Cannot leave the comment empty"
        }, status=status.HTTP_400_BAD_REQUEST)

    content = data.get("content")

    if not content:
        return Response({
            "message": "Cannot leave the comment empty"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        ad_comment = AdComment.objects.create(
            content=content,
            ad=ad,
            user=user,
        )
        send_comment_notification.delay(ad_id=ad.pk, comment_id=ad_comment.pk)
        return Response({
            "messages": "comment added successfully",
            "data": AdCommentSerializer(ad_comment, many=False).data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while adding the comment, try again please."
        }, status=status.HTTP_400_BAD_REQUEST)
