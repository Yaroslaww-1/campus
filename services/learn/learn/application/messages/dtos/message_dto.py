from pydantic import BaseModel
from datetime import datetime


class MessageDto(BaseModel):
    message_id: str
    chat_id:str
    created_by: str
    created_at: datetime
    content:str

