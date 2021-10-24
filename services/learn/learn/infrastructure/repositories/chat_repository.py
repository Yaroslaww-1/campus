from typing import List
from django.forms import model_to_dict

from services.learn.learn.domain.Chat.entities.chat import Chat
from services.learn.learn.domain.users.value_objects.user_id import UserId
from services.learn.learn.domain.Chat.value_objects.chat_id import ChatId
from services.learn.learn.models import Chat as ChatModel
from services.learn.learn.infrastructure.repositories.user_repository import UserRepository


class ChatRepository:
    @staticmethod
    def model_to_entity(model:ChatModel)->Chat:
        return Chat(
            chat_id=ChatId(model.chat_id),
            name=model.name,
            is_group_chat=model.is_group_chat,
            created_by=UserId(model.created_by)
        )

    @staticmethod
    def entity_to_model(entity: Chat) -> Chat:
        return ChatModel(
            chat_id = entity.chat_id.value,
            name = entity.name,
            is_group_chat = entity.is_group_chat,
            created_by = UserRepository.entity_to_model(entity.created_by)
        )


    def get_chats(self)->List[Chat]:
        chats = ChatModel.objects.all()
        return list(map(self.model_to_entity, chats))


    def get_chat_by_id(self, chat_id) -> Chat:
        temp_chat = ChatModel.objects.get(chat_id=chat_id)
        return self.model_to_entity(temp_chat)


    def save_or_update_chat(self, chat: Chat) -> None:
        ChatModel.objects.update_or_create(model_to_dict((self.entity_to_model(chat)), id = chat.chat_id.value))