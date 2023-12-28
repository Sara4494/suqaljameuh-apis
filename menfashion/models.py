from django.db import models
from Ad.models import Ad
from varieties.models import SubType, Mechanism

# Create your models here.


class Fashion(Ad):
    mechanism = models.ForeignKey(
        Mechanism, on_delete=models.CASCADE, null=True)
    subtype = models.ForeignKey(SubType, on_delete=models.CASCADE, null=True)
