from django.db import models
from Ad.models import Ad
from varieties.models import Capacity
# Create your models here.


class Electronics(Ad):
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)
