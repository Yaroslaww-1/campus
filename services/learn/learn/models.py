import uuid

from django.db import models

# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "user"
    objects = models.Manager()


class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(null=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "post"
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
        db_table = "student_group"

    objects = models.Manager()
