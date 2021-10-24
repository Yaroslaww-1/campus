from typing import List

from services.learn.learn.application.user_chats.dtos.user_chat_dto import UserChatDto
from services.learn.learn.domain.user_chat.entities.user_chat import UserChat


class UserChatMapper:
    @staticmethod
    def to_dto(entity: UserChat) -> UserChatDto:
        return UserChatDto(
            user_chat_id = entity.user_chat_id.value,
            chat_id = entity.chat_id.value,
            user_id = entity.user_id.value
       )

    @staticmethod
    def to_dto(entities: List[UserChat]) -> List[UserChatDto]:
        return list(map(UserChatMapper.to_dto, entities))