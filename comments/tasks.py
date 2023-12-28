from celery import shared_task
from notification.models import Notification, NotificationSettings
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from Ad.models import Ad
from django.core import exceptions
from comments.models import AdComment

@shared_task
def send_comment_notification(ad_id, comment_id):
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        print("Ad NOT FOUND")

    try:
        comment = AdComment.objects.get(pk=comment_id)
    except exceptions.ObjectDoesNotExist:
        print("Ad NOT FOUND")

    if ad.user == comment.user:
        return

    try:
        notification_settings = NotificationSettings.objects.get(
            user__id=ad.user.pk)
    except NotificationSettings.DoesNotExist:
        print("the notification settings doesn't exists")

    try:
        if not notification_settings.comments_alert:
            return
        group_name = f"user-{ad.user.pk}-notification"
        notification = Notification.objects.create(
            content=f"{comment.user} commented on your ad {ad.ad_title}",
            to_user=ad.user
        )
        channel_layer = get_channel_layer()

        event = {
            "type": "notification",
            "content": notification.content,
            "read": notification.read,
            "sent_at": notification.sent_at,
        }

        async_to_sync(channel_layer.group_send)(
            group_name, event
        )
    except Exception as e:
        print(f"an error occurred while sending notification {e}")
