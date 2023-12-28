from celery import shared_task
from notification.models import Notification
from users.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from reports.models import *


@shared_task(bind=False)
def send_admin_report_notification(report_id, content):
    try:
        report = ReportAd.objects.get(id=report_id)
        notification = Notification.objects.create(
            to_user=report.reported_by,
            content=content
        )
        channel_layer = get_channel_layer()
        users = User.objects.filter(is_superuser=True)
        for user in users:
            admin_notifications_group = f'admin-{user.pk}-notifications'
            async_to_sync(channel_layer.group_send)(
                admin_notifications_group,
                {
                    'type': 'report_notification',
                    'message': notification.content
                }
            )
        return "Admin notification sent"
    except Exception as e:
        print(f"Error: {str(e)}")


@shared_task
def send_user_report_notification(report_id, content):
    try:
        try:
            report = ReportAd.objects.get(id=report_id)
        except ReportAd.DoesNotExist:
            print("Report not found")

        notification = Notification.objects.create(
            to_user=report.reported_by, content=content

        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'user-{report.reported_by.pk}-notification',
            {
                'type': 'notification',
                'text': notification.content
            }
        )
        print("User notification sent")
    except Exception as e:
        print(f"Error: {str(e)}")


@shared_task
def send_admin_problem_notification(self, problem_id, content):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        notification = Notification.objects.create(
            to_user=problem.reported_by,
            content=content
        )
        channel_layer = get_channel_layer()
        users = User.objects.filter(is_superuser=True)
        for user in users:
            admin_notifications_group = f'admin-{self.id}-notifications'
            async_to_sync(channel_layer.group_send)(
                admin_notifications_group,
                {
                    'type': 'problem_notification',
                    'message': notification.content
                }
            )
        return "Admin notification sent"
    except Exception as e:
        print(f"Error: {str(e)}")


@shared_task
def send_user_problemt_notification(problem_id, self, content):
    try:
        problem = ReportProblem.objects.get(id=problem_id)
        notification = Notification.objects.create(
            to_user=problem.reported_by, content=content

        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'user-{self.user.id}-notification',
            {
                'type': 'notification',
                'text': notification.content
            }
        )
        return "User notification sent"
    except Exception as e:
        print(f"Error: {str(e)}")
