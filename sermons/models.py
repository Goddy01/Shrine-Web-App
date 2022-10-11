from email.policy import default
from django.db import models
import uuid
from ckeditor.fields import RichTextField
from datetime import date
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify

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
    slug =                  models.SlugField(blank=True, unique=True, max_length=255)

    @property
    def is_past_due(self):
        """To confirm if a sermon has taken place"""
        return date.today() > self.sermon_date

@receiver(post_delete, sender=Sermon)
def submission_delete(sender, instance, **kwargs):
    """Deletes the image of a sermon when the correlating Sermon is deleted"""
    instance.image.delete(False)

def pre_save_sermon_receiver(sender, instance, **kwargs):
    """Checks if a sermon has a slug, if not it creates one. This executes before each sermon is commited to the database"""
    if not instance.slug:
        instance.slug = slugify(instance.sermon_id)
pre_save.connect(pre_save_sermon_receiver, sender=Sermon)