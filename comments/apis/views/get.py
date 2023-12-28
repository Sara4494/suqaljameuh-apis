from Ad.models import Ad
from comments.models import AdComment
from comments.apis.serializers import AdCommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.core import exceptions

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_user_comments(request):
    user = request.user
    try:
        comments = AdComment.objects.filter(ad__user=user).order_by("-commented_at")
        serializer = AdCommentSerializer(comments, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting the comments"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_ad_comments(request, ad_id):
    
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "This ad doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        comments = AdComment.objects.filter(ad=ad).order_by("-commented_at")
        serializer = AdCommentSerializer(comments, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting the comments"
        }, status=status.HTTP_400_BAD_REQUEST)
