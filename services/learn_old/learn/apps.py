import inject
from django.apps import AppConfig


class LearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learn'

    def ready(self):
        inject.configure_once(self.configure)
        self._subscribe_to_domain_events()

    def configure(self, binder):
        self._configure_infrastructure(binder)
        self._configure_application(binder)

    def _configure_infrastructure(self, binder):
        # Options
        from learn.api.options.rabbit_mq_options import RabbitMQOptions
        binder.bind_to_constructor(RabbitMQOptions, RabbitMQOptions)

        # Event Bus
        from learn.infrastructure.event_bus.integration.integration_event_bus import IntegrationEventBus
        from learn.infrastructure.event_bus.domain.domain_event_bus import DomainEventBus
        from learn.infrastructure.event_bus.integration.rabbitmq.rabbitmq_integration_event_bus import \
            RabbitMQIntegrationEventBus
        from learn.infrastructure.event_bus.integration.rabbitmq.rabbit_mq_connection_factory import RabbitMQConnectionFactory
        binder.bind_to_constructor(RabbitMQConnectionFactory, RabbitMQConnectionFactory)
        rabbit_mq_connection_factory = RabbitMQConnectionFactory(RabbitMQOptions())
        rabbit_mq_integration_event_bus = RabbitMQIntegrationEventBus(rabbit_mq_connection_factory)
        binder.bind_to_constructor(IntegrationEventBus, rabbit_mq_integration_event_bus)
        binder.bind_to_constructor(DomainEventBus, DomainEventBus)

        # Repositories
        from learn.infrastructure.repositories.group_repository import GroupRepository
        from learn.infrastructure.repositories.post_repository import PostRepository
        from learn.infrastructure.repositories.student_repository import StudentRepository
        from learn.infrastructure.repositories.user_repository import UserRepository
        from learn.infrastructure.repositories.role_repository import RoleRepository
        binder.bind_to_constructor(PostRepository, PostRepository)
        binder.bind_to_constructor(UserRepository, UserRepository)
        binder.bind_to_constructor(StudentRepository, StudentRepository)
        binder.bind_to_constructor(GroupRepository, GroupRepository)
        binder.bind_to_constructor(RoleRepository, RoleRepository)

    def _configure_application(self, binder):
        # Domain Events
        from learn.domain.common.domain_events import DomainEventHandler
        from learn.domain.posts.events.post_created_domain_event import PostCreatedDomainEvent
        from learn.application.posts.domain_event_handlers.post_created_domain_event_handler import \
            PostCreatedDomainEventHandler
        binder.bind_to_constructor(DomainEventHandler[PostCreatedDomainEvent], PostCreatedDomainEventHandler)

        # Integration Events
        from learn.infrastructure.event_bus.integration.integration_event_handler import IntegrationEventHandler
        from learn.application.users.integration_events.user_created.user_created_integration_event import \
            UserCreatedIntegrationEvent
        from learn.application.users.integration_events.user_created.user_created_integration_event_handler import \
            UserCreatedIntegrationEventHandler
        binder.bind_to_constructor(IntegrationEventHandler["UserCreatedIntegrationEvent"], UserCreatedIntegrationEventHandler)

    def _subscribe_to_domain_events(self):
        from learn.application.users.integration_events.user_created.user_created_integration_event import \
            UserCreatedIntegrationEvent
        from learn.infrastructure.event_bus.integration.rabbitmq.rabbitmq_integration_event_bus import \
            RabbitMQIntegrationEventBus
        integration_event_bus = inject.get_injector().get_instance(RabbitMQIntegrationEventBus)
        integration_event_bus.start_consuming()
        integration_event_bus.subscribe(UserCreatedIntegrationEvent.type())
