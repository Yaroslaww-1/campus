from typing import List
from django.forms import model_to_dict

from services.learn.learn.domain.Chat.entities.chat import Chat
from services.learn.learn.domain.Chat.value_objects.chat_id import ChatId
from services.learn.learn.models import Chat as ChatModel, UserChat as UserChatModel
from services.learn.learn.infrastructure.repositories.user_repository import UserRepository


class ChatRepository:
    @staticmethod
    def model_to_entity(model: ChatModel, uc_model: UserChatModel) -> Chat:
        return Chat(
            chat_id=ChatId(model.id),
            name=model.name,
            is_group_chat=model.is_group_chat,
            created_by=UserRepository.model_to_entity(model.created_by),
            members=UserRepository.model_to_entity(uc_model.objects.filter(chat_id = ChatId(model.id)).user)
        )


    @staticmethod
    def entity_to_model(entity: Chat) -> ChatModel:
        return ChatModel(
            chat_id=entity.chat_id.value,
            name=entity.name,
            is_group_chat=entity.is_group_chat,
            created_by=UserRepository.entity_to_model(entity.created_by)
        )


    def get_chats(self) -> List[Chat]:
        chats = ChatModel.objects.all()
        return list(map(self.model_to_entity, chats))

    def get_chat_by_id(self, chat_id) -> Chat:
        temp_chat = ChatModel.objects.get(chat_id=chat_id)
        return self.model_to_entity(temp_chat)

    def save_chat(self, chat: Chat) -> None:
        temp_chat = self.entity_to_model(chat)
        ChatModel.objects.update_or_create(
            chat_id=temp_chat.chat_id,
            name=temp_chat.name,
            is_group_chat=temp_chat.is_group_chat,
            created_by=temp_chat.created_by
        )

    def update_chat(self, chat: Chat) -> None:
        ChatModel.objects.filter(id=chat.chat_id.value).update(model_to_dict(self.entity_to_model(chat)))
