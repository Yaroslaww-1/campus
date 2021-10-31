from typing import List
import inject

from services.learn.learn.application.messages.dtos.message_dto import  MessageDto
from services.learn.learn.application.messages.message_mapper import  MessageMapper
from services.learn.learn.infrastructure.repositories.message_repository import MessageRepository


class GetMessageQuery:
    @inject.autoparams()
    def __init__(self, message_rep: MessageRepository):
        self.message_rep = message_rep

    def execute(self) -> List[MessageDto]:
        message = self.message_rep.get_message()
        return MessageMapper.to_dtos(message)