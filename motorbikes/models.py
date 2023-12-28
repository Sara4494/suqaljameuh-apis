from django.db import models
from Ad.models import Ad
from varieties.models import KiloMeter, Capacity
# Create your models here.


class MotorBikes(Ad):
    kilo_meter = models.ForeignKey(
        KiloMeter, on_delete=models.CASCADE, null=True)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE, null=True)
