from django.db import models
from users.models import User

# Create your models here.


class Notification (models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content}'


class NotificationSettings(models.Model):
    private_message_notify = models.BooleanField(default=True, null=True)
    paid_service_alert = models.BooleanField(default=True, null=True)
    comments_alert = models.BooleanField(default=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.pk}'
