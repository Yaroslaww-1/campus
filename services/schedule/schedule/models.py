import uuid

from django.db import models

# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "role"

    objects = models.Manager()


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = "user"

    objects = models.Manager()


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "student"

    objects = models.Manager()


class EventType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "event_type"

    objects = models.Manager()


class EventTemplate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField()

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)

    class Meta:
        db_table = "event_template"

    objects = models.Manager()


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    time = models.DateTimeField()

    template = models.ForeignKey(EventTemplate, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    objects = models.Manager()


