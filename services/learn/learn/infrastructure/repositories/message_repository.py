from typing import List
from django.forms import model_to_dict

from services.learn.learn.domain.message.entities.message import Message
from services.learn.learn.domain.message.value_objects.message_id import MessageId
from services.learn.learn.infrastructure.repositories.user_repository import UserRepository
from services.learn.learn.infrastructure.repositories.chat_repository import ChatRepository
from services.learn.learn.models import User as UserModel, Chat as ChatModel, Message as MessageModel


class MessageRepository:
    @staticmethod
    def model_to_entity(model:MessageModel) -> Message:
        return Message(
            message_id=MessageId(model.message_id),
            chat_id=ChatRepository.model_to_entity(model.chat_id),
            created_by=UserRepository.model_to_entity(model.created_by),
            create_on=model.created_at,
            content=model.content,
        )

    @staticmethod
    def entity_to_model(entity:Message) -> Message:
        return MessageModel(
            message_id = entity.message_id.value,
            created_by = entity.created_by.value,
            chat_id = entity.chat_id.value,
            created_at = entity.create_on,
            content = entity.content
        )

    def get_message(self) -> List[Message]:
        temp_messages = MessageModel.objects.all()
        return list(map(self.model_to_entity, temp_messages))

    def get_message_by_id(self, temp_id) -> Message:
        message = MessageModel.objects.get(id=temp_id)
        return self.model_to_entity(message)

    def save_or_update_message(self, message:Message) -> None:
        MessageModel.objects.update_or_create(model_to_dict(self.entity_to_model(message)), id=message.message_id.value)