import inject

from services.learn.learn.application.chats.dtos.chats_dto import ChatDto
from services.learn.learn.application.chats.chat_mapper import ChatMapper
from services.learn.learn.infrastructure.repositories.chat_repository import ChatRepository


class GetChatById:
    @inject.autoparams()
    def __init__(self, chat_rep: ChatRepository):
        self.chat_rep = chat_rep

    def execute(self, temp_id) -> ChatDto:
        chat = self.chat_rep.get_chat_by_id(temp_id)
        return ChatMapper.to_dto(chat)
