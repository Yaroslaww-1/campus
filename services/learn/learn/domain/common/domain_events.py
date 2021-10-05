import uuid
from typing import List, TypeVar, Generic, Type, Callable


T = TypeVar("T")


class DomainEvent:
    def __init__(self):
        self.id = uuid.uuid4()


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


class Handler(Generic[T]):
    """Simple generic used to associate handlers with events using DI.
    e.g Handler[AuctionEnded].
    """
    pass
