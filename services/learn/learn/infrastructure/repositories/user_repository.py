from typing import List

from learn.domain.users.entities.user import User
from learn.domain.users.value_objects.user_id import UserId
from learn.domain.users.value_objects.email import Email
from learn.models import User as UserModel


class UserRepository:
    def __init__(self):
        pass

    @staticmethod
    def model_to_entity(user_model: UserModel) -> User:
        id = UserId(user_model.id)
        email = Email(user_model.email)
        return User(
            id=id,
            name=user_model.name,
            email=email
        )

    def get_users(self) -> List[User]:
        users = UserModel.objects.all()
        return list(map(self.model_to_entity, users))

    def save_user(self, user: User) -> None:
        UserModel.objects.update_or_create(
            id=user.id.value,
            name=user.name,
            email=user.email.value
        )
