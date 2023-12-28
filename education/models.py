from django.db import models
from Ad.models import Ad
from varieties.models import Site

# Create your models here.


class Education(Ad):
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)
