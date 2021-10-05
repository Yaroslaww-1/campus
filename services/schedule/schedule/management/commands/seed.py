import datetime

from django.utils import timezone
import uuid

from django.core.management.base import BaseCommand
import random
import logging

from schedule.models import Teacher, User, Event, EventType

logger = logging.getLogger(__name__)


# python manage.py seed


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self)
        self.stdout.write('done.')


def clear_data():
    logger.info("Delete Teachers")
    Teacher.objects.all().delete()

    logger.info("Delete Users")
    User.objects.all().delete()

    logger.info("Delete Events")
    Event.objects.all().delete()

    logger.info("Delete EventTypes")
    EventType.objects.all().delete()


def create_users():
    logger.info("Creating users")

    user = User(
        id=uuid.uuid4(),
        name="Michael Jackson",
    )
    user.save()

    user = User(
        id=uuid.uuid4(),
        name="Paul McCartney",
    )
    user.save()

    user = User(
        id=uuid.uuid4(),
        name="John Lennon",
    )
    user.save()

    logger.info("Users created")


def create_event_types():
    logger.info("Creating EventTypes")

    event_type = EventType(
        id=uuid.uuid4(),
        name="Pair",
    )
    event_type.save()

    event_type = EventType(
        id=uuid.uuid4(),
        name="Exam",
    )
    event_type.save()

    logger.info("EventTypes created")


def create_events():
    logger.info("Creating events")

    event_types_count = EventType.objects.count()

    event_type = EventType.objects.all()[random.randint(0, event_types_count - 1)]
    event = Event(
        id=uuid.uuid4(),
        name="Pair 1",
        description="Pair 1 description",
        time=datetime.datetime.now(),
        type=event_type
    )
    event.save()

    event_type = EventType.objects.all()[random.randint(0, event_types_count - 1)]
    event = Event(
        id=uuid.uuid4(),
        name="Pair 2",
        description="Pair 2 description",
        time=datetime.datetime.now(),
        type=event_type
    )
    event.save()

    logger.info("Events created")


def create_teachers():
    logger.info("Creating teachers")

    users_count = User.objects.count()

    events = Event.objects.all()
    user = User.objects.all()[random.randint(0, users_count - 1)]
    teacher = Teacher(
        id=uuid.uuid4(),
        user=user,
    )
    teacher.save()
    teacher.events.add(events[0])

    logger.info("Teachers created")


# def create_teacher_events():
#     logger.info("Creating teacher_events")
#
#     teachers_count = Teacher.objects.count()
#     events_count = Event.objects.count()
#
#     teacher = Teacher.objects.all()[random.randint(0, teachers_count - 1)]
#     event = Event.objects.all()[random.randint(0, events_count - 1)]
#     teacher_event = TeacherEvent(
#         id=uuid.uuid4(),
#         teacher=teacher,
#         event=event
#     )
#     teacher_event.save()
#
#     teacher = Teacher.objects.all()[random.randint(0, teachers_count - 1)]
#     event = Event.objects.all()[random.randint(0, events_count - 1)]
#     teacher_event = Event(
#         id=uuid.uuid4(),
#         teacher=teacher,
#         event=event
#     )
#     teacher_event.save()
#
#     logger.info("teacher_events created")


def run_seed(self):
    clear_data()
    create_users()
    create_event_types()
    create_events()
    create_teachers()
