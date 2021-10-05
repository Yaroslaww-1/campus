import uuid

from django.db import models

# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class EventType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "event_type"

    objects = models.Manager()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    objects = models.Manager()


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "user"

    objects = models.Manager()


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, db_table="teacher_to_event")

    class Meta:
        db_table = "teacher"

    objects = models.Manager()


