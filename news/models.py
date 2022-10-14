from ckeditor.fields import RichTextField
import uuid
from django.db import models

# Create your models here.
class News(models.Model):
    news_id =           models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    news_headline =     models.CharField(max_length=256, blank=False, null=False)
    news_body =         RichTextField(max_length=20000, blank=False, null=False)
    date_posted =       models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.news_id