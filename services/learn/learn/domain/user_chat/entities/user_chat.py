import uuid

from services.learn.learn.domain.users.value_objects.user_id import UserId
from services.learn.learn.domain.user_chat.value_objects.user_chat_id import UserChatId
from services.learn.learn.domain.Chat.value_objects.chat_id import ChatId

class UserChat:
    def __init__(self, user_chat_id: UserChatId, chat_id:ChatId, user_id:UserId):
        self.user_chat_id = user_chat_id
        self.chat_id = chat_id
        self.user_id = user_id


    @classmethod
    def create_new_user_chat(cls, chat_id:ChatId, user_id:UserId) -> "UserChat":
        user_chat_id = UserChatId(value=uuid.uuid4())
        user_chat = UserChat(user_chat_id, chat_id, user_id)
        return user_chat