from email.policy import default
from django.db import models
import uuid
from ckeditor.fields import RichTextField
from datetime import date
# Create your models here.
def upload_location(instance, filename):
    return f'sermons/{str(instance.sermon_id)}-{filename}'

class Sermon(models.Model):
    sermon_id =             models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    sermon_title =          models.CharField(max_length=256, null=False, blank=False)
    sermon_priest_name =    models.CharField(max_length=128, null=False, blank=False)
    sermon_date =           models.DateField(max_length=128, null=False, blank=False)
    sermon_image =          models.ImageField(upload_to=upload_location, null=False, blank=False)
    sermon_desc =           models.TextField(max_length=1000, null=False, blank=False)
    sermon_body =           RichTextField(max_length=20000, blank=True, null=True)

    @property
    def is_past_due(self):
        """To confirm if a sermon has taken place"""
        return date.today() > self.sermon_date