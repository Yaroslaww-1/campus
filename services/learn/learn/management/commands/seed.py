from django.utils import timezone
import uuid

from django.core.management.base import BaseCommand
import random
import logging

from learn.models import Post, User, Group, Student, Role

logger = logging.getLogger(__name__)


# python manage.py seed


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self)
        self.stdout.write('done.')


def clear_data():
    logger.info("Delete Posts")
    Post.objects.all().delete()

    logger.info("Delete Students")
    Student.objects.all().delete()

    logger.info("Delete Users")
    User.objects.all().delete()

    logger.info("Delete Roles")
    Role.objects.all().delete()

    logger.info("Delete Groups")
    Group.objects.all().delete()


def create_roles():
    logger.info("Creating roles")

    role = Role(
        id=uuid.uuid4(),
        name="Admin",
    )
    role.save()

    role = Role(
        id=uuid.uuid4(),
        name="Student",
    )
    role.save()

    role = Role(
        id=uuid.uuid4(),
        name="Teacher",
    )
    role.save()

    logger.info("Roles created")


def create_users():
    logger.info("Creating users")

    role = Role.objects.get(name="Admin")
    user = User(
        id="11111111-1111-1111-1111-111111111111",
        name="Admin",
        email="admin@gmail.com",
        avatar=None
    )
    user.save()
    user.roles.set([role])

    role = Role.objects.get(name="Teacher")
    user = User(
        id="22222222-2222-2222-2222-222222222222",
        name="Teacher",
        email="teacher@gmail.com",
        avatar=None
    )
    user.save()
    user.roles.set([role])

    role = Role.objects.get(name="Student")
    user = User(
        id="33333333-3333-3333-3333-333333333333",
        name="Student",
        email="student@gmail.com",
        avatar=None
    )
    user.save()
    user.roles.set([role])

    logger.info("Users created")


def create_posts():
    logger.info("Creating posts")

    created_by = User.objects.get(id="22222222-2222-2222-2222-222222222222")
    post = Post(
        id=uuid.uuid4(),
        name="1st lab",
        content="First lab will be available at the end of today",
        created_at=timezone.now(),
        created_by=created_by
    )
    post.save()

    created_by = User.objects.get(id="22222222-2222-2222-2222-222222222222")
    post = Post(
        id=uuid.uuid4(),
        name="Pair link",
        content="Pair link is here",
        created_at=timezone.now(),
        created_by=created_by
    )
    post.save()

    created_by = User.objects.get(id="22222222-2222-2222-2222-222222222222")
    post = Post(
        id=uuid.uuid4(),
        name="Dopka(",
        content="Vseh na dopku =(",
        created_at=timezone.now(),
        created_by=created_by
    )
    post.save()

    logger.info("Posts created")


def create_groups():
    logger.info("Creating groups")
    group = Group(
        id=uuid.uuid4(),
        name="IP-96",
        formed_at_year=2019
    )
    group.save()

    group = Group(
        id=uuid.uuid4(),
        name="IP-92",
        formed_at_year=2019
    )
    group.save()

    group = Group(
        id=uuid.uuid4(),
        name="IP-91",
        formed_at_year=2019
    )
    group.save()

    logger.info("Groups created")


def create_students():
    logger.info("Creating students")

    user = User.objects.get(id="33333333-3333-3333-3333-333333333333")
    group = Group.objects.get(name="IP-96")
    student = Student(
        id=uuid.uuid4(),
        user=user,
        group=group
    )
    student.save()

    logger.info("Students created")


def run_seed(self):
    clear_data()
    create_roles()
    create_users()
    create_groups()
    create_students()
    create_posts()
