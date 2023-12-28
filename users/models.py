from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    full_name = models.CharField(verbose_name="Full Name", max_length=50)
    email = models.EmailField(verbose_name="Email",
                              max_length=200, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(verbose_name='Phone_Number', max_length=50)
    birth_date = models.DateTimeField(auto_now_add=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=50)

    city = models.ForeignKey(
        'varieties.City', null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(
        'varieties.Country', null=True, on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        'self', related_name='following', symmetrical=False)
    followings = models.ManyToManyField(
        'self', related_name='follower', symmetrical=False)

    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'male'), ('female', 'female')))
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # indicator to indicate whether the user is verified or not
    is_verified = models.BooleanField(default=False)
    # indicator toe indicate whether the user is suspended or not
    is_suspended = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email
