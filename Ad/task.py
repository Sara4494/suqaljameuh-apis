from celery import shared_task
from .models import Notification
from users.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task(bind=True)
def SendNotification(self, user_id) :
    main_user = User.objects.get(id=user_id)
    
    users_followers_list = main_user.followers.all() 


    channel_layer = get_channel_layer() 
    if users_followers_list :
        for user in users_followers_list :
            content = f'New Ad was create from {main_user.full_name}'
            Notification.objects.create(
                to_user = user,
                content = content
            ).save()

            group_name = f'user-{user.id}-notification'
            event = {
                'type':'notification',
                'text' : content
            }

            async_to_sync(channel_layer.group_send)(
                group_name,event
            )

    return "Done"
    