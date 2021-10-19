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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_group"

    objects = models.Manager()


class Chat(models.Model):
    chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    is_group_chat = models.NullBooleanField(blank=True)
    created_by = models.UUIDField(default=uuid.uuid4())

    class Meta:
        db_table = "Chat"

    objects = models.Manager()


class UserChat(models.Model):
    user_chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE())

    class Meta:
        db_table = "UserChat"

    objects = models.Manager()


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    created_by = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='created_by')
    created_on = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='created_on')
    content = models.TextField(null=False)

    class Meta:
        db_table = "Message"

    objects = models.Manager()