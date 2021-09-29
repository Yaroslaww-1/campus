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
