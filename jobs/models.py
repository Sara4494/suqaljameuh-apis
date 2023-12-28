from django.db import models
from varieties.models import Country, City, Currency
from Ad.models import Ad
from users.models import User
# Create your models here.
from django.db import models

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

SOCIAL_STATUS = (
    ("Single", "Single"),
    ("Married", "Married"),
)

READY_STATUS = (
    ("Start Now", "Start Now"),
    ("Available But Not On The Spot", "Available But Not On The Spot"),
)

COMPANY_TYPES = (
    ("Individual", "Individual"),
    ("Employment Company", "Employment Company"),
    ("Company", "Company"),
)

SHIT_SYSTEM = (
    ("Limited Working Hours", "Limited Working Hours"),
    ("Shits", "Shits"),
    ("Hourly", "Hourly"),
)

class JobTitle(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class JobSector(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class Grade(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class ExperienceLevel(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class PreviousExp(models.Model):
    job_title = models.CharField(max_length=320, null=True)
    company_name = models.CharField(max_length=120, null=True)
    description = models.CharField(max_length=255, null=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)

class PreviousCourse(models.Model):
    course_title = models.CharField(max_length=320, null=True)
    company_name = models.CharField(max_length=120, null=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class Language(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class ContractType(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )


class WorkingHours(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )
from django.db import models

# ...

class JobSeeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, null=True)
    phone_number = models.BigIntegerField()
    bio = models.TextField()
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    job_sector = models.ForeignKey(JobSector, on_delete=models.CASCADE)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="seeker_nationality")
    residence_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    residence_city = models.ForeignKey(City, on_delete=models.CASCADE)
    can_shift = models.BooleanField(default=False )
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=50)
    social_status = models.CharField(choices=SOCIAL_STATUS, max_length=50)
    ready_status = models.CharField(choices=READY_STATUS, max_length=50)
    age = models.IntegerField()
    skills = models.ManyToManyField(Skill, default=True)
    salary = models.BigIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    has_vehicle = models.BooleanField(default=False )
    has_license = models.BooleanField(default=False )
    working_hours = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)
    work_from_home = models.BooleanField(default=False )
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    exp_level = models.ForeignKey(ExperienceLevel, on_delete=models.CASCADE)
    prev_exp = models.ForeignKey(PreviousExp, on_delete=models.CASCADE)
    prev_course = models.ForeignKey(PreviousCourse, on_delete=models.CASCADE)
    cv = models.FileField(upload_to="cvs/")
    published_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Benefit(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(default=False )

class JobOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_type = models.CharField(choices=COMPANY_TYPES, max_length=50)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    job_sector = models.ForeignKey(JobSector, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(City, on_delete=models.CASCADE)
    working_days = models.IntegerField()
    work_from_home = models.BooleanField(default=False )
    shift_system = models.CharField(choices=SHIT_SYSTEM, max_length=50)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    salary = models.BigIntegerField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    benefits = models.ManyToManyField(Benefit, default=True)
    exp_level = models.ForeignKey(ExperienceLevel, on_delete=models.CASCADE)
    require_vehicle = models.BooleanField(default=False )
    require_license = models.BooleanField(default=False )
    gender = models.CharField(choices=GENDER, max_length=50)
    languages = models.ManyToManyField(Language, default=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, default=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name="offer_country")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name="offer_city")
    job_description = models.TextField()
    phone_number = models.BigIntegerField()
    published_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)