# Generated by Django 4.1.1 on 2022-10-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='date_posted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
