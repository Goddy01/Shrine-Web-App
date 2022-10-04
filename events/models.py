from django.db import models
import uuid

# Create your models here.
class Event(models.Model):
    event_id =          models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    event_name =        models.CharField(max_length=256, null=False, blank=False)
    event_date =        models.CharField(max_length=128, null=False, blank=False)
    event_time =        models.CharField(max_length=128, null=False, blank=False)
    event_location =    models.CharField(max_length=128, null=False, blank=False)
    event_url =         models.URLField(max_length=256)
    event_description = models.TextField(max_length=10000, blank=False, null=False)

    def __str__(self):
        return self.event_id