# Generated by Django 4.1.1 on 2022-10-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0007_alter_donate_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]