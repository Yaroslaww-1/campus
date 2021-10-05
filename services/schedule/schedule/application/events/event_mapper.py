from typing import List

from schedule.application.events.dtos.event_dto import EventDto
from schedule.domain.events.entities.event import Event


class EventMapper:
    @staticmethod
    def to_dto(entity: Event) -> EventDto:
        return EventDto(
            id=entity.id.value,
            name=entity.name,
            description=entity.description,
            time=entity.time,
            type=entity.type.value
        )

    @staticmethod
    def to_dtos(entities: List[Event]) -> List[EventDto]:
        return list(map(EventMapper.to_dto, entities))
