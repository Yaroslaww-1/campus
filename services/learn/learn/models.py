import uuid

from django.db import models

# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "role"

    def publish(self) -> str:
        return 'a'

    # objects = models.Manager()


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

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


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "chat"

    objects = models.Manager()


class UserChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "user_chat"

    objects = models.Manager()


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    content = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "message"

    objects = models.Manager()


class GroupSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "group_schedule"

    objects = models.Manager()


class UserSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    group = models.ForeignKey(GroupSchedule, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "user_schedule"

    objects = models.Manager()


class EventTypeSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "event_type_schedule"

    objects = models.Manager()


class EventSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    teacher = models.ForeignKey(UserSchedule, on_delete=models.CASCADE, unique=True)
    event_type = models.ForeignKey(EventTypeSchedule, on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "event_schedule"

    objects = models.Manager()
