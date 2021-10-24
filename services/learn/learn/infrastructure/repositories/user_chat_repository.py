from typing import List
from django.forms import model_to_dict

from services.learn.learn.infrastructure.repositories.user_repository import UserRepository
from services.learn.learn.infrastructure.repositories.chat_repository import ChatRepository
from services.learn.learn.models import User as UserModel, Chat as ChatModel, UserChat as UCModel
from services.learn.learn.domain.user_chat.entities.user_chat import UserChat
from services.learn.learn.domain.user_chat.value_objects.user_chat_id import UserChatId


class UserChatRepository:
    @staticmethod
    def model_to_entity(model: UCModel,  user_model: UserModel) -> UserChat:
        return UserChat(
            user_chat_id= UserChatId(model.user_chat_id),
            chat_id=ChatRepository.model_to_entity(model.chat_id),
            user_id=UserRepository.model_to_entity(model.user_id)
        )

    @staticmethod
    def entity_to_model(entity: UserChat) -> UserChat:
        return UCModel(
           user_chat_id=entity.message_id.value,
            chat_id=entity.chat_id.value,
            user_id = entity.user_id.value
        )

    def save_user_chat(self, user_chat: UserChat) -> None:
        UCModel.objects.update_or_create(
            user_chat_id = user_chat.user_chat_id.value,
            chat_id = UCModel.objects.get(chat_id = user_chat.chat_id.value),
            user_id = UCModel.objects.get(user_id = user_chat.user_id.value)
        )

    def get_user_chat(self) -> List[UserChat]:
        temp_user_chats = UCModel.objects.all()
        return list(map(self.model_to_entity, temp_user_chats))

    def save_or_update_user_chat(self, user_chat: UserChat) -> None:
        UCModel.objects.update_or_create(model_to_dict(self.entity_to_model(user_chat)), id=user_chat.user_chat_id.value)

    def get_user_chat_by_id(self, temp_id) -> UserChat:
        user_chat = UCModel.objects.get(id=temp_id)
        return self.model_to_entity(user_chat)