from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from notification.models import NotificationSettings
from users.permissions import UserOwnerOnly, UserActive


@api_view(["PUT",])
@permission_classes([UserActive, UserOwnerOnly])
def update_notification(request):
    user = request.user
    data = request.data

    try:
        notification_settings = NotificationSettings.objects.get(user=user)
    except NotificationSettings.DoesNotExist:
        return Response({
            "message": "The settings is not found"
        }, status=status.HTTP_404_NOT_FOUND)

    if not data:
        return Response({
            "message": "Nothing to update"
        }, status=status.HTTP_400_BAD_REQUEST)

    private_message_notify = data.get("private_message_notify")
    paid_service_alert = data.get("paid_service_alert")
    comments_alert = data.get("comments_alert")
    print(paid_service_alert)
    try:
        is_updated = False
        if private_message_notify != None and notification_settings.private_message_notify != private_message_notify:
            notification_settings.private_message_notify = private_message_notify
            is_updated = True
        if paid_service_alert != None and notification_settings.paid_service_alert != paid_service_alert:
            notification_settings.paid_service_alert = paid_service_alert
            is_updated = True
        if private_message_notify != None and notification_settings.comments_alert != comments_alert:
            notification_settings.comments_alert != comments_alert
            is_updated = True
        if is_updated == True:
            notification_settings.save()
            return Response({
                "message": "your notification settings were updated successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "nothing was updated"
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(e)
        return Response({
            'message': 'an error occurred while updating the settings'
        }, status=status.HTTP_400_BAD_REQUEST)
