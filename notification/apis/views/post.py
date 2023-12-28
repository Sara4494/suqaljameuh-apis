from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from notification.models import Notification
from users.permissions import UserOwnerOnly, UserActive


@api_view(["POST", "PUT"])
@permission_classes([UserActive, UserOwnerOnly])
def mark_notifications_asread(request):
    try:
        notifications = Notification.objects.filter(to_user=request.user)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting all the notifications"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        for notification in notifications:
            notification.read = True
            notification.save()
    except Exception as e:
        return Response({
            "message": "an error occurred while seeing all the notifications"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST", "PUT"])
@permission_classes([permissions.IsAuthenticated])
def mark_notification_asread(request, notification_id):
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        return Response({
            "message": "notification not found"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        notification.read = True
        notification.save()
    except Exception as e:
        return Response({
            "message": "an error occurred while seeing the notification"
        }, status=status.HTTP_400_BAD_REQUEST)
