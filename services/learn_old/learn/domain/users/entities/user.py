import uuid
from typing import List

from learn.domain.users.entities.role import Role
from learn.domain.users.value_objects.email import Email
from learn.domain.users.value_objects.user_id import UserId


class User:
    def __init__(self, id: UserId, name: str, email: Email, roles: List[Role], avatar: str = None):
        self.id = id
        self.name = name
        self.email = email
        self.roles = roles
        self.avatar = avatar

    @classmethod
    def create_new_user(cls, name: str, email: str, roles: List[Role]) -> "User":
        id = UserId(value=uuid.uuid4())
        email = Email(value=email)
        user = User(id, name, email, roles)
        return user

    @classmethod
    def initialize(cls, id: UserId, name: str, email: str, roles: List[Role]) -> "User":
        email = Email(value=email)
        user = User(id, name, email, roles)
        return user

    def set_avatar(self, avatar: str) -> None:
        self.avatar = avatar
