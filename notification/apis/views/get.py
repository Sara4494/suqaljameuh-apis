from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from notification.models import NotificationSettings
from notification.apis.serializers import NotificationSettingSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_notification_settings(request):
    user = request.user

    try:
        notification_settings = NotificationSettings.objects.get(user=user)
    except NotificationSettings.DoesNotExist:
        return Response({
            "message": "The settings is not found"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        serializer = NotificationSettingSerializer(
            notification_settings, many=False).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"an error occurred while getting the notification settings"
        }, status=status.HTTP_400_BAD_REQUEST)
