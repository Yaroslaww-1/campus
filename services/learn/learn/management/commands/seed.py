from django.utils import timezone
import uuid

from django.core.management.base import BaseCommand
import random
import logging

from learn.models import Post, User, Group, StudentGroup

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

    logger.info("Delete Users")
    User.objects.all().delete()

    logger.info("Delete Groups")
    Group.objects.all().delete()

    logger.info("Delete StudentsGroup")
    StudentGroup.objects.all().delete()


def create_users():
    logger.info("Creating users")

    user = User(
        id=uuid.uuid4(),
        name="Michael Jackson",
        email="mj@gmail.com"
    )
    user.save()

    user = User(
        id=uuid.uuid4(),
        name="Paul McCartney",
        email="paul@gmail.com"
    )
    user.save()

    user = User(
        id=uuid.uuid4(),
        name="John Lennon",
        email="john@gmail.com"
    )
    user.save()

    logger.info("Users created")


def create_posts():
    logger.info("Creating posts")
    users_count = User.objects.count()

    created_by = User.objects.all()[random.randint(0, users_count - 1)]
    post = Post(
        id=uuid.uuid4(),
        name="1st lab",
        content="First lab will be available at the end of today",
        created_at=timezone.now(),
        created_by=created_by
    )
    post.save()

    created_by = User.objects.all()[random.randint(0, users_count - 1)]
    post = Post(
        id=uuid.uuid4(),
        name="Pair link",
        content="Pair link is here",
        created_at=timezone.now(),
        created_by=created_by
    )
    post.save()

    created_by = User.objects.all()[random.randint(0, users_count - 1)]
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


def create_students_group():
    logger.info("Creating students_group")

    user = User.objects.get(name="Michael Jackson")
    group = Group.objects.get(name="IP-96")
    student_group = StudentGroup(
        id=uuid.uuid4(),
        user=user,
        group=group
    )
    student_group.save()

    user = User.objects.get(name="John Lennon")
    group = Group.objects.get(name="IP-91")
    student_group = StudentGroup(
        id=uuid.uuid4(),
        user=user,
        group=group
    )
    student_group.save()

    user = User.objects.get(name="Paul McCartney")
    group = Group.objects.get(name="IP-92")
    student_group = StudentGroup(
        id=uuid.uuid4(),
        user=user,
        group=group
    )
    student_group.save()

    logger.info("Students_group created")


def run_seed(self):
    clear_data()
    create_users()
    create_groups()
    create_students_group()
    create_posts()
