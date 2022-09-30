from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
# Create your models here.
class UserProfile(models.Model):
    user =          models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =    models.CharField(max_length=128, null=False)
    last_name =     models.CharField(max_length=128, null=False)
    username =      models.CharField(unique=True, max_length=128, null=False)
    email =         models.EmailField(unique=True, null=False)
    country =       CountryField(max_length=255, null=False, blank=False)
    phone_number =  PhoneNumberField(unique=True, null=False)
    date_joined =   models.DateTimeField(auto_now_add=True)
    last_login =    models.DateTimeField(auto_now=True)
    is_admin =      models.BooleanField(default=False)
    is_staff =      models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    is_superuser =  models.BooleanField(default=False)
    is_worshipper = models.BooleanField(default=True)

    def __str__(self):
        return self.username