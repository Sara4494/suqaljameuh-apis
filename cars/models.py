from django.db import models
from Ad.models import Ad
from varieties.models import KiloMeter, RentPeriod

# Create your models here.


class TransmissionType(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class FoulType(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class BodyType(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)
    icon = models.ImageField(upload_to="body-types/")


class RegionalSpecs(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class InternalSpecs(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class OuterSpecs(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Car(Ad):
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    foul_type = models.ForeignKey(FoulType, on_delete=models.CASCADE)
    transmission_type = models.ForeignKey(
        TransmissionType, on_delete=models.CASCADE)
    rent_period = models.ForeignKey(RentPeriod, on_delete=models.CASCADE)
    is_rental = models.BooleanField(default=False)
    regional_specs = models.ForeignKey(RegionalSpecs, on_delete=models.CASCADE)
    internal_specs = models.ManyToManyField(InternalSpecs)
    outer_specs = models.ManyToManyField(OuterSpecs)
    car_number = models.CharField(max_length=520)
    kilo_meter = models.ForeignKey(KiloMeter, on_delete=models.CASCADE)
