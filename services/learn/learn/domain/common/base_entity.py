import uuid


class BaseEntity:
    def __init__(self, id: uuid.UUID):
        self.id = id
