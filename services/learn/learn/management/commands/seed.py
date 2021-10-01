from django.utils import timezone
import uuid

from django.core.management.base import BaseCommand
import random
import logging

from learn.models import Post, User

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

    user = User.objects.all()[random.randint(0, users_count - 1)]
    post = Post(
        id=uuid.uuid4(),
        name="1st lab",
        content="First lab will be available at the end of today",
        created_at=timezone.now(),
        user=user
    )
    post.save()

    user = User.objects.all()[random.randint(0, users_count - 1)]
    post = Post(
        id=uuid.uuid4(),
        name="Pair link",
        content="Pair link is here",
        created_at=timezone.now(),
        user=user
    )
    post.save()

    user = User.objects.all()[random.randint(0, users_count - 1)]
    post = Post(
        id=uuid.uuid4(),
        name="Dopka(",
        content="Vseh na dopku =(",
        created_at=timezone.now(),
        user=user
    )
    post.save()

    logger.info("Posts created")


def run_seed(self):
    clear_data()
    create_users()
    create_posts()
