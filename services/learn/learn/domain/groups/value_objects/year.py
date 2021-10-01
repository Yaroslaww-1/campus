from pydantic import ValidationError


class Year:
    def __init__(self, value: int):
        if 2010 < value < 2100:
            raise ValidationError
        else:
            self.value = value
