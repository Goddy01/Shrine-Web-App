from email.policy import default
from django.db import models
import uuid
# Create your models here.
class Donation(models.Model):
    donation_id =           models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    donation_name =         models.CharField(max_length=256, null=False, blank=False)
    donation_desc =         models.TextField(max_length=5000, blank=False, null=False)
    amounted_needed =       models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.donation_id