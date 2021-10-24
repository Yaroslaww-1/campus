from pydentic import BaseModel


class ChatDto(BaseModel):
    chat_id: str
    name: str
    is_group_chat: bool
    created_by: str
