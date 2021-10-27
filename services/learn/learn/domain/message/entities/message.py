import uuid
from django.utils.datetime_safe import datetime

from services.learn.learn.domain.users.value_objects.user_id import UserId
from services.learn.learn.domain.Chat.value_objects.chat_id import ChatId
from services.learn.learn.domain.message.value_objects.message_id import MessageId

class Message:
    def __init__(self, message_id: MessageId, chat_id: ChatId, created_by:UserId, create_on:datetime, content: str):
        self.message_id = message_id
        self.chat_id = chat_id
        self.created_by = created_by
        self.create_on = create_on
        self.content = content


    @classmethod
    def create_new_message(cls, content: str, chat_id: ChatId, created_by:UserId) -> "Message":
        message_id = MessageId(value=uuid.uuid4())
        message = Message(message_id, chat_id,  created_by, datetime.now(),  content)
        return message