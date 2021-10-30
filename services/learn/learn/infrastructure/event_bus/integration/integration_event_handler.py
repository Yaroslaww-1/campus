from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict

E = TypeVar('E')


class IntegrationEventHandler(ABC, Generic[E]):
    @abstractmethod
    def handle(self, event: Dict):
        raise NotImplementedError()