import uuid


class BaseTypedIdValueObject:
    def __init__(self, value: uuid.UUID):
        self._value = value

    @property
    def value(self) -> str:
        return self._value.hex
