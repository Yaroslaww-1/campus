from pydantic import BaseModel


class UserChatDto(BaseModel):
    user_chat_id: str
    chat_id: str
    user_id: str