from django.core.exceptions import ValidationError


class Year:
    def __init__(self, value: int):
        if 2010 < value < 2100:
            self.value = value
        else:
            raise ValidationError("Invalid year")
