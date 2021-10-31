from abc import ABC, abstractmethod
from typing import TypeVar

from learn.infrastructure.event_bus.integration.integration_event_handler import IntegrationEventHandler

E = TypeVar('E')


class IntegrationEventBus(ABC):
    @abstractmethod
    def subscribe(self, event: E):
        raise NotImplementedError()
