from typing import List

from services.learn.learn.application.chats.dtos.chat_dto import ChatDto
from services.learn.learn.domain.Chat.entities.chat import Chat


class ChatMapper:
    @staticmethod
    def to_dto(entity: Chat) -> ChatDto:
        return ChatDto(
            chat_id=entity.chat_id.value,
            name=entity.name,
            is_group_chat = entity.is_group_chat,
            created_by=entity.created_by.value
        )

    @staticmethod
    def to_dto(entities: List[Chat]) -> List[ChatDto]:
        return list(map(ChatMapper.to_dto, entities))