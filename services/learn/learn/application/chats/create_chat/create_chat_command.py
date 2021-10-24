import inject
from pydantic import BaseModel, StrictStr


from services.learn.learn.application.chats.dtos.chat_dto import ChatDto
from services.learn.learn.application.chats.chat_mapper import ChatMapper
from services.learn.learn.domain.Chat.entities.chat import Chat
from services.learn.learn.infrastructure.repositories.chat_repository import ChatRepository


class CreateChatCommandDto(BaseModel):
    name: StrictStr
    is_group_chat: bool
    created_by: StrictStr



class CreateChatCommand:
    @inject.autoparams()
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def execute(self, dto: CreateChatCommandDto) -> ChatDto:
        chat = Chat.create_new_chat(name=dto.name, is_group_chat=dto.is_group_chat, created_by=dto.created_by)
        self.chat_repository.save_or_update_chat(chat)
        return ChatMapper.to_dto(chat)
