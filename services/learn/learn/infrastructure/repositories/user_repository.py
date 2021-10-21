from typing import List

from learn.domain.users.entities.user import User
from learn.domain.users.value_objects.user_id import UserId
from learn.domain.users.value_objects.email import Email
from learn.models import User as UserModel


class UserRepository:
    @staticmethod
    def model_to_entity(model: UserModel) -> User:
        return User(
            id=UserId(model.id),
            name=model.name,
            email=Email(model.email),
        )

    @staticmethod
    def entity_to_model(entity: User) -> User:
        return UserModel(
            id=entity.id.value,
            name=entity.name,
            email=entity.email.value
        )

    def get_users(self) -> List[User]:
        users = UserModel.objects.all()
        return list(map(self.model_to_entity, users))

    def get_user_by_id(self, id) -> User:
        user = UserModel.objects.get(id=id)
        return self.model_to_entity(user)

    def save_user(self, user: User) -> None:
        UserModel.objects.update_or_create(self.entity_to_model(user))

    def save_user_avatar(self, id, imageUrl: str) -> None:
        UserModel.objects.filter(id=id).update(avatar=imageUrl)
