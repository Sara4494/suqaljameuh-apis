from .bridge import Bridge
from django.db import models
from polymorphic.models import PolymorphicModel
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


from django.core.validators import MaxValueValidator, MinValueValidator
from varieties.models import *


AD_TYPES = (
    ("Very Featured", "Very Featured"),
    ("Featured", "Featured"),
    ("Free", "Free"),
)


class Ad (PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=100)
    ad_description = models.TextField(max_length=1000)
    price = models.FloatField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    phone_number = models.BigIntegerField(null=True)
    active = models.BooleanField(default=True)
    rating = models.BigIntegerField(default=0, validators=[
        MaxValueValidator(5), MinValueValidator(0)])
    ratings_count = models.BigIntegerField(default=0)
    brand = models.ForeignKey(
        Brand, null=True, on_delete=models.CASCADE, blank=True)
    model = models.ForeignKey(
        Model, null=True, on_delete=models.CASCADE, blank=True)
    material = models.ForeignKey(
        Material, null=True, on_delete=models.CASCADE, blank=True)
    type = models.ForeignKey(
        Type, null=True, on_delete=models.CASCADE, blank=True)
    top_style = models.ForeignKey(
        TopStyle, null=True, on_delete=models.CASCADE, blank=True)
    condition = models.ForeignKey(
        Condition, null=True, on_delete=models.CASCADE, blank=True)
    size = models.ForeignKey(
        Size, null=True, on_delete=models.CASCADE, blank=True)
    color = models.ForeignKey(
        Colors, null=True, on_delete=models.CASCADE, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    lat = models.CharField(max_length=200, null=True)
    lat_delta = models.CharField(max_length=200, null=True)
    long = models.CharField(max_length=200, null=True)
    long_delta = models.CharField(max_length=200, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True)
    ad_type = models.CharField(
        max_length=70, choices=AD_TYPES, default=AD_TYPES[2][1])
    is_delivery = models.BooleanField(default=False, null=True)
    active = models.BooleanField(default=False)

    published_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.ad_title}"


class AdPicture(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='ads-images/', null=True, blank=True)


class RateAd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                           related_name="ad_ratings")
    rate = models.IntegerField(max_length=5)
    rated_at = models.DateField(auto_now_add=True)


@receiver(post_save, sender=Ad)
def Send_Message_To_Ad_Owner_Followers(created, instance, **kwrags):
    if created:
        user_id = instance.user.id
        try:
            Bridge(user_id=user_id)

        except Exception as error:
            print(f"An error accoured : {error}")
