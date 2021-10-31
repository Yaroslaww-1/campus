import datetime
import uuid


class IntegrationEvent:
    def __init__(self):
        self.id = uuid.uuid4()
        self.occurred_on = datetime.datetime.now()

    @staticmethod
    def type():
        raise NotImplementedError()
