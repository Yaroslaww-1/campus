import inject
from django.apps import AppConfig


class LearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learn'

    def ready(self):
        inject.configure_once(self.configure_di)

    def configure_di(self, binder):
        from learn.application.posts.domain_event_handlers.post_created_domain_event_handler import \
            PostCreatedDomainEventHandler
        from learn.domain.common.domain_events import Handler
        from learn.domain.posts.events.post_created_domain_event import PostCreatedDomainEvent
        from learn.infrastructure.events.event_bus import EventBus
        from learn.infrastructure.repositories.group_repository import GroupRepository
        from learn.infrastructure.repositories.post_repository import PostRepository
        from learn.infrastructure.repositories.student_repository import StudentRepository
        from learn.infrastructure.repositories.user_repository import UserRepository

        # Infrastructure
        binder.bind_to_constructor(EventBus, EventBus)
        binder.bind_to_constructor(PostRepository, PostRepository)
        binder.bind_to_constructor(UserRepository, UserRepository)
        binder.bind_to_constructor(StudentRepository, StudentRepository)
        binder.bind_to_constructor(GroupRepository, GroupRepository)
        # Application
        binder.bind_to_constructor(Handler[PostCreatedDomainEvent], PostCreatedDomainEventHandler)
