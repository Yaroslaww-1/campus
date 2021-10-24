import uuid

from services.learn.learn.domain.users.value_objects.user_id import UserId
from services.learn.learn.domain.Chat.value_objects.chat_id import ChatId


class Chat:
    def __init__(self, chat_id: ChatId, name: str, is_group_chat:bool, created_by:UserId):
        self.chat_id = chat_id
        self.name = name
        self.is_group_chat = is_group_chat
        self.created_by = created_by

    @classmethod
    def create_new_chat(cls, name: str, is_group_chat:bool, created_by:UserId) -> "Chat":
        chat_id = ChatId(value=uuid.uuid4())
        chat = Chat(chat_id, name, is_group_chat,  created_by)
        return chat