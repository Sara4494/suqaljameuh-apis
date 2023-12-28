from django.db import models
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from notification.models import NotificationSettings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to='profile-images/', null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    facebook_acc = models.URLField(null=True, blank=True)
    instagram_acc = models.URLField(null=True, blank=True)
    whatsapp = models.IntegerField(null=True, blank=True)
    cv_file = models.FileField(upload_to='cv-files', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def CreateCustomProfile(created, instance, **kwargs):
    try:
        NotificationSettings.objects.get_or_create(user=instance)
        gender = instance.gender
        profile = Profile.objects.create(user=instance)
        if gender:
            profile.picture = f"profile-images/{gender}.png"
        profile.picture = f"profile-images/male.png"

        profile.save()
    except Exception as e:
        print(
            f"an error occurred while executing celery task, creating custom user profile: {e}")
