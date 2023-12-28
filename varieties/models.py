from django.db import models
from users.models import User


class Category (models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="categories-images/")
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class SubCategory (models.Model):
    category = models.ForeignKey(
        Category, related_name='sub_category_model', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Brand (models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="brand-images/")
    added_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class RentPeriod(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Capacity(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


class KiloMeter(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class OS(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Memory(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Storage(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)


class Material (models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Type (models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class SubType(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)


class TopStyle (models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Condition (models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)
    category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class Site(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Size (models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Colors (models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Qualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    started_at = models.DateField()
    graduate_at = models.DateField()


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    intro_number = models.IntegerField()
    flag = models.ImageField(upload_to='flag/', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    country = models.ForeignKey(
        Country, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Mechanism(models.Model):
    name = models.CharField(max_length=150)
    added_at = models.DateField(auto_now_add=True)
    is_enabled = models.BooleanField(default=True)
