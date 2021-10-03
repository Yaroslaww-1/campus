import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)

    objects = models.Manager()


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    objects = models.Manager()


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    formed_at_year = models.IntegerField()

    class Meta:
        db_table = "group"

    objects = models.Manager()


class StudentGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = "studentGroup"

    objects = models.Manager()
