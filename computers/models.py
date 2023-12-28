from django.db import models
from Ad.models import Ad
from varieties.models import OS, Storage, Memory

# Create your models here.


class ScreenSize(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Computer(Ad):
    os = models.ForeignKey(OS, on_delete=models.CASCADE, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True)
    screen_size = models.ForeignKey(
        ScreenSize, on_delete=models.CASCADE, null=True)
