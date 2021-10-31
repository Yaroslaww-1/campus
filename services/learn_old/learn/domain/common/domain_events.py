import uuid
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Type, Callable


T = TypeVar("T")
E = TypeVar('E')


class DomainEvent:
    def __init__(self):
        self.id = uuid.uuid4()


class DomainEventHandler(ABC, Generic[E]):
    @abstractmethod
    def handle(self, event: E):
        raise NotImplementedError()


class WithDomainEventsMixin:
    def __init__(self) -> None:
        self._pending_domain_events: List[DomainEvent] = []

    def add_domain_event(self, event: DomainEvent) -> None:
        self._pending_domain_events.append(event)

    @property
    def domain_events(self) -> List[DomainEvent]:
        return self._pending_domain_events[:]

    def clear_domain_events(self) -> None:
        self._pending_domain_events.clear()
