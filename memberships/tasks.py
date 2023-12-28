from celery import shared_task
from asgiref.sync import async_to_sync
from notification.models import Notification
from channels.layers import get_channel_layer
from .models import *
from users.models import User
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import FeaturedMember


@shared_task
def send_notification_after_sub(user_id, membership_name):
    """
    this task is responsible for sending notifications after 
    subscribing in any of the existing membership plans
    """
    print("HEYYYYYYYYYYYYY")
    try:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print("user doesn't exists")
        group_name = f"user-{user_id}-notification"
        channel_layer = get_channel_layer()
        notification = Notification.objects.create(
            content=f"Congrats! You're now subscribed in {membership_name} plan, you can enjoy its features now",
            to_user=user
        )

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
        print("an error occurred while sending the user a notification regarding his subscription:", e)


@shared_task
def check_featured_memberships():
    try:
        today = datetime.now().date()

        # Get expired featured memberships and send notifications to the associated users
        expired_featured_memberships = FeaturedMember.objects.filter(
            subscription_expiration=today)
        for membership in expired_featured_memberships:
            try:

                user = membership.subscriber
                notification = Notification.objects.create(
                    to_user=user,
                    content='Your featured membership has expired'
                )
                membership.subscriber.user_rank = "Normal"
                membership.delete()
                # Send notification to the user
                channel_layer = get_channel_layer()
                notifications_group = f'user-{user.id}-notification'

                async_to_sync(channel_layer.group_send)(
                    notifications_group,
                    {
                        'type': 'notification',
                        'text': notification.content,
                    }
                )
            except Exception as e:
                # Handle any errors that occur during notification sending
                print(
                    f'Error sending notification to user {user.id}: {str(e)}')

    except Exception as e:
        # Handle any other exceptions that occur during the execution
        print(f'Error in check_featured_memberships: {str(e)}')


@shared_task
def manage_user_memberships():
    try:
        today = datetime.now().date()

        # Delete expired user memberships
        expired_user_memberships = UserMembership.objects.filter(
            subscription_expiration=today)
        for membership in expired_user_memberships:
            user = membership.subscriber
            notification = Notification.objects.create(
                to_user=user,
                content='Your membership will expire in 1 day'
            )
            try:
                # Send notification to the user
                channel_layer = get_channel_layer()
                notifications_group = f'user-{user.id}-notification'

                async_to_sync(channel_layer.group_send)(
                    notifications_group,
                    {
                        'type': 'notification',
                        'text': notification.content,
                    }
                )
            except Exception as e:
                # Handle any errors that occur during notification sending
                print(
                    f'Error sending notification to user {user.id}: {str(e)}')
    except Exception as e:
        # Handle any other exceptions that occur during the execution
        print(f'Error in manage_user_memberships: {str(e)}')
