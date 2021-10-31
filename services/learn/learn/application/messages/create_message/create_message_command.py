import inject
from pydantic import BaseModel, StrictStr
from datetime import datetime

from services.learn.learn.application.messages.dtos.message_dto import MessageDto
from services.learn.learn.application.messages.message_mapper import MessageMapper
from  services.learn.learn.domain.message.entities.message import Message
from  services.learn.learn.infrastructure.repositories.message_repository import MessageRepository


class CreateMessageCommandDto(BaseModel):
   create_at: datetime
   content: StrictStr


class CreateMessageCommand:
    @inject.autoparams()
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def execute(self, dto: CreateMessageCommandDto) -> MessageDto:
        message = Message.create_new_message(create_on=dto.create_at, content=dto.content)
        self.message_repository.save_or_update_message(message)
        return MessageMapper.to_dto(message)