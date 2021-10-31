from typing import List

from services.learn.learn.application.messages.dtos.message_dto import MessageDto
from services.learn.learn.domain.message.entities.message import Message


class MessageMapper:
    @staticmethod
    def to_dto(entity: Message) -> MessageDto:
        return MessageDto(
            message_id = entity.message_id.value,
            chat_id = entity.chat_id.value,
            created_by = entity.created_by.value,
            created_at = entity.create_on,
            content = entity.content,
        )


    @staticmethod
    def to_dtos(entities: List[Message]) -> List[MessageDto]:
        return list(map(MessageMapper.to_dto, entities))