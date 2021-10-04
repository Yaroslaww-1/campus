import logging
from typing import List

import inject

from learn.domain.common.domain_events import DomainEvent, Handler


class EventBus:
    def process_domain_event(self, event: DomainEvent) -> None:
        logging.info(f"start processing domain event, {event}")
        injector = inject.get_injector()
        handler = injector.get_instance(Handler[type(event)])
        handler.handle(event)
        logging.info(f"end processing domain event, {event}")

    def process_domain_events(self, events: List[DomainEvent]) -> None:
        for event in events:
            self.process_domain_event(event)
