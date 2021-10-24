from typing import List
import inject

from services.learn.learn.application.user_chats.dtos.user_chat_dto import  UserChatDto
from services.learn.learn.application.user_chats.user_chat_mapper import  UserChatMapper
from services.learn.learn.infrastructure.repositories.user_chat_repository import UserChatRepository


class GetUserChatQuery:
    @inject.autoparams()
    def __init__(self, user_chat_rep: UserChatRepository):
        self.user_chat_rep = user_chat_rep

    def execute(self) -> List[UserChatDto]:
        user_chats = self.user_chat_rep.get_user_chat()
        return UserChatMapper.to_dto(user_chats)