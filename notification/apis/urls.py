from django.urls import path
from notification.apis.views.get import get_notification_settings
from notification.apis.views.update import update_notification
from notification.apis.views.post import mark_notification_asread, mark_notifications_asread


urlpatterns = [
    path("get/", get_notification_settings),
    path("update/", update_notification),
    path("mark-notifications-asread/", mark_notifications_asread),
    path("mark-notification-asread/<int:notification_id>/", mark_notification_asread),
]