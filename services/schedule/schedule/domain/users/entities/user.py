import uuid

from schedule.domain.users.value_objects.user_id import UserId


class User:
    def __init__(self, id: UserId, name: str):
        self.id = id
        self.name = name

    @classmethod
    def create_new_user(cls, name: str) -> "User":
        id = UserId(value=uuid.uuid4())
        user = User(id, name)
        return user
