import inject
from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'

    def ready(self):
        inject.configure_once(self.configure_di)

    def configure_di(self, binder):
        from schedule.infrastructure.events.event_bus import EventBus
        from schedule.infrastructure.repositories.user_repository import UserRepository
        from schedule.infrastructure.repositories.event_repository import EventRepository

        # Infrastructure
        binder.bind_to_constructor(EventBus, EventBus)
        binder.bind_to_constructor(UserRepository, UserRepository)
        binder.bind_to_constructor(EventRepository, EventRepository)
