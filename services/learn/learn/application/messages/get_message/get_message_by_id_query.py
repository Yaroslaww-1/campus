import inject

from services.learn.learn.application.messages.dtos.message_dto import  MessageDto
from services.learn.learn.application.messages.message_mapper import  MessageMapper
from services.learn.learn.infrastructure.repositories.message_repository import MessageRepository

class GetMessageById:
    @inject.autoparams()
    def __init__(self, message_rep: MessageRepository):
        self.message_rep = message_rep

    def execute(self, temp_id) -> MessageDto:
        message = self.message_rep.get_message_by_id(temp_id = temp_id)
        return MessageMapper.to_dto(message)