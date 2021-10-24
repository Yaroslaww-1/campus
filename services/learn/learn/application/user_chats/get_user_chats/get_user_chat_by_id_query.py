import inject

from services.learn.learn.application.user_chats.dtos.user_chat_dto import  UserChatDto
from services.learn.learn.application.user_chats.user_chat_mapper import  UserChatMapper
from services.learn.learn.infrastructure.repositories.user_chat_repository import UserChatRepository

class GetUserChatById:
    @inject.autoparams()
    def __init__(self, user_chat_rep: UserChatRepository):
        self.user_chat_rep = user_chat_rep

    def execute(self, temp_id) -> UserChatDto:
        user_chat = self.user_chat_rep.get_user_chat_by_id(temp_id)
        return UserChatMapper.to_dto(user_chat)