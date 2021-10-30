from typing import Dict

import inject

from learn.application.users.integration_events.user_created.user_created_integration_event import \
    UserCreatedIntegrationEvent
from learn.domain.users.entities.user import User
from learn.domain.users.value_objects.user_id import UserId
from learn.infrastructure.event_bus.integration.integration_event_handler import IntegrationEventHandler
from learn.infrastructure.repositories.role_repository import RoleRepository
from learn.infrastructure.repositories.user_repository import UserRepository


class UserCreatedIntegrationEventHandler(IntegrationEventHandler):
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository, role_repository: RoleRepository):
        self._user_repository = user_repository
        self._role_repository = role_repository

    def handle(self, event: Dict):
        print("process")
        event = UserCreatedIntegrationEvent(**event)

        roles = self._role_repository.get_roles()
        user_roles = [role for role in roles if role.name in event.roles]

        user = User.initialize(
            id=UserId(event.user_id),
            name=event.name,
            email=event.email,
            roles=user_roles
        )

        self._user_repository.create(user)
