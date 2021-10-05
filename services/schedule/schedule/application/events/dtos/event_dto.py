from pydantic import BaseModel

from schedule.domain.common.typings import DateTime


class EventDto(BaseModel):
    id: str
    name: str
    description: str
    time: DateTime
    type: str
