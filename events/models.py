import datetime
from django.core.exceptions import ValidationError
from django.db import models
import uuid

# Create your models here.
def validate_date(date):
    if date < datetime.datetime.now().date():
        raise ValidationError("Date cannot be in the past")
class Event(models.Model):
    event_id =          models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    event_name =        models.CharField(max_length=256, null=False, blank=False)
    event_date =        models.DateField(max_length=128, null=False, blank=False, default=None, validators=[validate_date])
    event_time =        models.CharField(max_length=128, null=False, blank=False)
    event_location =    models.CharField(max_length=128, null=False, blank=False)
    event_url =         models.URLField(max_length=256, null=True, blank=True)
    event_description = models.TextField(max_length=10000, blank=False, null=False)

    def __str__(self):
        return self.event_id