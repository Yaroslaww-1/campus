from typing import List

from schedule.domain.common.typings import DateTime
from schedule.domain.events.entities.event import Event
from schedule.domain.events.value_objects.event_id import EventId
from schedule.domain.events.value_objects.event_type import EventType
from schedule.models import Event as EventModel, EventType as EventTypeModel


class EventRepository:
    @staticmethod
    def model_to_entity(model: EventModel) -> Event:
        return Event(
            id=EventId(model.id),
            name=model.name,
            description=model.description,
            time=DateTime(model.time),
            type=EventType(model.type.name)
        )

    def get_events(self) -> List[Event]:
        events = EventModel.objects.all()
        return list(map(self.model_to_entity, events))
