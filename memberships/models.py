from django.db import models
from users.models import User

# Create your models here.


class Membership(models.Model):
    name = models.CharField(max_length=150, verbose_name="Membership Name")
    price = models.BigIntegerField()
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)



class MembershipFeature(models.Model):
    membership = models.ForeignKey(
        Membership, on_delete=models.CASCADE, related_name="membership_features")
    feature = models.CharField(max_length=450)


class UserMembership(models.Model):
    subscriber = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="membership")
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    subscription_expiration = models.DateTimeField(null=True, blank=True)


class FeaturedMembership(models.Model):
    name = models.CharField(max_length=150, verbose_name="Membership Name")
    price = models.DecimalField(
        verbose_name="Membership price", max_digits=5, decimal_places=3)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

class FeaturedMembershipFeature(models.Model):
    membership = models.ForeignKey(
        FeaturedMembership, on_delete=models.CASCADE, related_name="membership_features")
    feature = models.CharField(max_length=450)


class FeaturedMember(models.Model):
    subscriber = subscriber = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(FeaturedMembership, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    subscription_expiration = models.DateTimeField(null=True, blank=True)

class AdMembership(models.Model):
    name = models.CharField(max_length=150, verbose_name="Membership Name")
    price = models.DecimalField(
        verbose_name="Membership price", max_digits=5, decimal_places=3)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

class AdMembership(models.Model):
    name = models.CharField(max_length=150, verbose_name="Membership Name")
    price = models.DecimalField(
        verbose_name="Membership price", max_digits=5, decimal_places=3)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

class AdMembershipFeature(models.Model):
    membership = models.ForeignKey(
        AdMembership, on_delete=models.CASCADE, related_name="membership_features")
    feature = models.CharField(max_length=450)
