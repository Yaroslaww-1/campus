from typing import List

import inject

from schedule.application.events.dtos.event_dto import EventDto
from schedule.application.events.event_mapper import EventMapper
from schedule.infrastructure.repositories.event_repository import EventRepository


class GetEventsQuery:
    @inject.autoparams()
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self) -> List[EventDto]:
        events = self.event_repository.get_events()
        return EventMapper.to_dtos(events)
