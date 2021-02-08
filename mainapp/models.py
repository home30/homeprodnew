from django.db import models
from phone_field import PhoneField


# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=30)
    prof_image = models.ImageField(null=True)
    job_title = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
