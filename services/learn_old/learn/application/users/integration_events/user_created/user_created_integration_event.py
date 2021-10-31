import datetime
import uuid
from typing import Any, List

from pydantic import BaseModel

from learn.infrastructure.event_bus.integration.integration_event import IntegrationEvent


class UserCreatedIntegrationEvent(BaseModel, IntegrationEvent):
    id: uuid.UUID
    occurred_on: datetime.datetime
    user_id: uuid.UUID
    name: str
    email: str
    roles: List[str]

    @staticmethod
    def type():
        return "UserCreatedIntegrationEvent"
