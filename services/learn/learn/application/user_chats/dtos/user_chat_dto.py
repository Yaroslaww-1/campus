from pydantic import BaseModel

from services.learn.learn.application.chats.dtos.chat_dto import ChatDto
from services.learn.learn.application.users.dtos.user_dto import UserDto

class UserChatDto(BaseModel):
    chat: ChatDto
    user: UserDto