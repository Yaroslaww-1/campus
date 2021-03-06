# Generated by Django 3.2.4 on 2021-10-04 17:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.UUIDField(default=uuid.UUID('00448f59-673f-402b-8014-f264e302be16'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learn.group'),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='id',
            field=models.UUIDField(default=uuid.UUID('688786a5-a7cb-4b7e-8727-c07511de2fbc'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learn.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8e93029b-c1fa-48d4-95fb-a9f18b68e939'), primary_key=True, serialize=False),
        ),
    ]
