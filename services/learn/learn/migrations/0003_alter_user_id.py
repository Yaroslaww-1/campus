# Generated by Django 3.2.4 on 2021-09-23 10:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('876f5c9e-17a3-4caf-9f10-9aeb359123a2'), primary_key=True, serialize=False),
        ),
    ]