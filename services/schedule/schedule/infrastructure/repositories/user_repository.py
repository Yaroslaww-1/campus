from typing import List

from schedule.domain.users.entities.user import User
from schedule.domain.users.value_objects.user_id import UserId
from schedule.models import User as UserModel


class UserRepository:
    @staticmethod
    def model_to_entity(model: UserModel) -> User:
        return User(
            id=UserId(model.id),
            name=model.name,
        )

    @staticmethod
    def entity_to_model(entity: User) -> User:
        return UserModel(
            id=entity.id.value,
            name=entity.name,
        )

    def get_users(self) -> List[User]:
        users = UserModel.objects.all()
        return list(map(self.model_to_entity, users))
