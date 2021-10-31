from typing import List

from services.learn.learn.application.chats.dtos.chats_dto import ChatDto, ChatMemberDto
from services.learn.learn.domain.Chat.entities.chat import Chat
from services.learn.learn.domain.users.entities.user import User


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
    def to_dtos(entities: List[Chat]) -> List[ChatDto]:
        return list(map(ChatMapper.to_dto, entities))


class ChatMemberMaper:
        @staticmethod
        def to_dto_member(entity: User) -> ChatMemberDto:
            return ChatMemberDto(
                id=entity.id,
                name=entity.name,
                avatar=entity.avatar
            )

        @staticmethod
        def to_dtos_member(entities: List[User]) -> List[ChatMemberDto]:
            return list(map(ChatMemberMaper.to_dto_member, entities))
