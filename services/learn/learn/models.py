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
    email = models.CharField(max_length=100)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = "user"

    objects = models.Manager()


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    formed_at_year = models.IntegerField()

    class Meta:
        db_table = "group"

    objects = models.Manager()


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = "student"

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


class Chat(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=False)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "chat"

    objects = models.Manager()


class UserChat(models.Model):
    id = models.UUIDField(primary_key=True)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_chat"

    objects = models.Manager()


class Message(models.Model):
    id = models.UUIDField(primary_key=True)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(null=False)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "message"

    objects = models.Manager()


class Course(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=False)

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "course"

    objects = models.Manager()


class CourseAssignment(models.Model):
    id = models.UUIDField(primary_key=True)
    deadline_at = models.DateTimeField(null=False)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_assignment"

    objects = models.Manager()


class CourseAssignmentSubmission(models.Model):
    id = models.UUIDField(primary_key=True)
    submitted_at = models.DateTimeField(null=False)
    content = models.TextField()

    assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_assignment_submission"

    objects = models.Manager()


class CourseAssignmentSubmissionReview(models.Model):
    id = models.UUIDField(primary_key=True)
    reviewed_at = models.DateTimeField(null=False)
    mark = models.IntegerField()

    submission = models.ForeignKey(CourseAssignmentSubmission, on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_assignment_submission_review"


objects = models.Manager()
