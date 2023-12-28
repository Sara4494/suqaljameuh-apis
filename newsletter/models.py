from django.db import models
from users.models import *
class Newsletter(models.Model):
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)