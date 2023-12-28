from django.db import models
from Ad.models import Ad
from users.models import User
# Create your models here.


class AdComment(models.Model):
    commented_at = models.DateField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    