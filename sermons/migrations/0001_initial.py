# Generated by Django 4.1.1 on 2022-10-10 09:09

import ckeditor.fields
from django.db import migrations, models
import sermons.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('sermon_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('sermon_title', models.CharField(max_length=256)),
                ('sermon_priest_name', models.CharField(max_length=128)),
                ('sermon_date', models.DateField(max_length=128)),
                ('sermon_image', models.ImageField(upload_to=sermons.models.upload_location)),
                ('sermon_desc', models.TextField(max_length=1000)),
                ('sermon_body', ckeditor.fields.RichTextField(blank=True, max_length=20000, null=True)),
            ],
        ),
    ]
