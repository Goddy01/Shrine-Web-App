from email.policy import default
from enum import auto
from django.db import models
from accounts.models import UserProfile
import uuid
# Create your models here.
class Donation(models.Model):
    donation_id =           models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    donation_name =         models.CharField(max_length=256, null=False, blank=False)
    donation_desc =         models.TextField(max_length=5000, blank=False, null=False)
    amount_needed =         models.IntegerField(null=False, blank=False)
    amount_raised =         models.IntegerField(null=True, default=0)
    date_posted =           models.DateTimeField(auto_now=True, null=True)
    complete =              models.BooleanField(default=False)
    def __str__(self):
        return self.donation_id

class Donate(models.Model):
    donated_id =            models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user =                  models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    amount_donated =        models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.donated_id