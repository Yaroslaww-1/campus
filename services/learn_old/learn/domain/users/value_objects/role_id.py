import uuid

from learn.domain.common.base_typed_id_value_object import BaseTypedIdValueObject


class RoleId(BaseTypedIdValueObject):
    def __init__(self, value: uuid.UUID):
        super().__init__(value)
