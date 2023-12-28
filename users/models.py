from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth import models as auth_model
import random


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


USER_RANKS = (
    ("Premium", "Premium"),
    ("Featured", "Featured"),
    ("Normal", "Normal")
)


class User(AbstractUser):
    username = None
    groups = None
    first_name = None
    last_name = None
    user_permissions = None

    full_name = models.CharField(verbose_name="Full Name", max_length=50)
    email = models.EmailField(verbose_name="Email",
                              max_length=200, unique=True)
    phone_number = models.CharField(
        verbose_name='Phone_Number', max_length=50, null=True)
    birth_date = models.DateField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False)
    ratings_count = models.BigIntegerField(default=0)
    rate = models.IntegerField(default=0)
    city = models.ForeignKey(
        'varieties.City', null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(
        'varieties.Country', null=True, on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        'self', related_name='followers_of',default=True, symmetrical=False, null=True)
    followings = models.ManyToManyField(
        'self', related_name='followings_of',default=True, symmetrical=False, null=True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'male'), ('female', 'female')), default="male", null=True)
    user_rank = models.CharField(
        max_length=10,
        choices=USER_RANKS,
        default="Normal"
    )
    # indicator to indicate whether the user is verified or not
    is_verified = models.BooleanField(default=False)

    # indicator toe indicate whether the user is suspended or not
    is_suspended = models.BooleanField(default=False)

    # This is the total points the user have earned over the time.
    points = models.BigIntegerField(default=0)
    USERNAME_FIELD = "email"
    objects = UserManager()
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email


class IntroVideo(models.Model):
    video = models.FileField(upload_to="intro-videos")
    added_at = models.DateField(auto_now_add=True)


class Rating(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ratings")
    rate = models.IntegerField(max_length=5)
    rated_at = models.DateField(auto_now_add=True)


class OTPCode(models.Model):
    otp = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True, null=True)
    valid_for = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.otp = code_string
        super().save(*args, **kwargs)
