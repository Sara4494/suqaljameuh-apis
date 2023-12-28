from django.db import models
from varieties.models import Country, Size, Amenity
from Ad.models import Ad
# Create your models here.

PUBLISHER = (
    ("The Owner", "The Owner"),
    ("The Mediator", "The Mediator"),
)


class NearLocation(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Interface(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class RoomCounts(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class BathroomCounts(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class FloorsCounts(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class BuildingAge(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class AdditionalFeature(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class AdjustedTo(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class EstateType(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class RealEstate(Ad):
    interface = models.CharField(max_length=250)
    near_location = models.ForeignKey(
        NearLocation, on_delete=models.CASCADE, null=True)
    rent_period = models.CharField(max_length=250)
    land_space = models.BigIntegerField(null=True)
    building_space = models.BigIntegerField(null=True)
    land_size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, null=True, related_name="land_size")
    building_size = models.ForeignKey(
        Size, on_delete=models.SET_NULL, null=True, related_name="building_size")
    bathroom_count = models.CharField(max_length=250)
    room_counts = models.CharField(max_length=250)
    floor_count = models.CharField(max_length=250)
    building_age = models.CharField(max_length=250)
    amenities = models.ManyToManyField(Amenity)
    # Add max_length attribute
    publisher = models.CharField(choices=PUBLISHER, null=True, max_length=100)
    is_mortgaged = models.BooleanField(null=True)
    additional_features = models.ManyToManyField(AdditionalFeature)
    is_rental = models.BooleanField(default=False)
    estate_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    estate_type = models.ForeignKey(EstateType, on_delete=models.CASCADE)
    adjusted_to = models.ForeignKey(AdjustedTo, on_delete=models.CASCADE)
