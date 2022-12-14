# Generated by Django 4.1.1 on 2022-10-15 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0003_rename_amounted_needed_donation_amount_needed'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='amount_raised',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Donated',
            fields=[
                ('donated_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('amount_donated', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
