from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

#manager for our custom model 
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Personal(models.Model):
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    photo = models.ImageField(upload_to='pro-pic')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    about = models.CharField(max_length=800)

class Education(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    start_on = models.CharField(max_length=100)
    end_on = models.CharField(max_length=100)
    percentage = models.FloatField()
    grade = models.CharField(max_length=10)

class Employment(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    fresher = models.CharField(max_length=10)
    work_exp = models.CharField(max_length=10)
    company_name = models.CharField(max_length=80)
    position = models.CharField(max_length=80)
    resp = models.CharField(max_length=200)
    start_on = models.CharField(max_length=100)
    end_on = models.CharField(max_length=100)

class Skill(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100)
    provide_by = models.CharField(max_length=100)

class Licence(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    license = models.CharField(max_length=100)
    provide_by = models.CharField(max_length=100)

class Reference(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    pincode = models.CharField(max_length=50)

class Social(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

class Language(models.Model):
    pid = models.OneToOneField(Personal, on_delete=models.CASCADE)
    Language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)