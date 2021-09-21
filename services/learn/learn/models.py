from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
