from django.db import models
from phone_field import PhoneField

class Contactus(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.CharField(max_length=100)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')


# Create your models here.
