import uuid

from schedule.domain.common.typings import DateTime
from schedule.domain.events.value_objects.event_id import EventId
from schedule.domain.events.value_objects.event_type import EventType


class Event:
    def __init__(self, id: EventId, name: str, description: str, time: DateTime, type: EventType):
        self.id = id
        self.name = name
        self.description = description
        self.time = time
        self.type =type

    @classmethod
    def create_new_user(cls, name: str, description: str, time: DateTime, type: str) -> "Event":
        id = EventId(value=uuid.uuid4())
        type = EventType(type)
        event = Event(id, name, description, time, type)
        return event
