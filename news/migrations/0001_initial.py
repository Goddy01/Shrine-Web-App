# Generated by Django 4.1.1 on 2022-10-14 21:09

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('news_headline', models.CharField(max_length=256)),
                ('news_body', ckeditor.fields.RichTextField(max_length=20000)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
