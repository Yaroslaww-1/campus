# Generated by Django 3.2.4 on 2021-10-04 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_switched_to_one_to_one'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.UUIDField(default=uuid.UUID('06d8ee6c-15d3-4275-abc3-e2b1474a251c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c407344b-2071-4ec0-904d-1053462a3b2c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ef3d516-4251-413e-a13d-d204fe698b6d'), primary_key=True, serialize=False),
        ),
    ]
