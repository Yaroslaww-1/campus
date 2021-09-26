import uuid

from learn.domain.users.value_objects.email import Email
from learn.domain.users.value_objects.user_id import UserId


class User:
    def __init__(self, id: UserId, name: str, email: Email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create_new_user(cls, name: str, email: str) -> "User":
        id = UserId(value=uuid.uuid4())
        email = Email(value=email)
        user = User(id, name, email)
        return user
