from typing import List

from django.forms import model_to_dict

from learn.domain.users.entities.user import User
from learn.domain.users.value_objects.user_id import UserId
from learn.domain.users.value_objects.email import Email
from learn.infrastructure.repositories.role_repository import RoleRepository
from learn.models import User as UserModel, Role as RoleModel


class UserRepository:
    @staticmethod
    def model_to_entity(model: UserModel, roles: List[RoleModel]) -> User:
        return User(
            id=UserId(model.id),
            name=model.name,
            email=Email(model.email),
            avatar=model.avatar,
            roles=RoleRepository.model_to_entities(roles)
        )

    @staticmethod
    def entity_to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id.value,
            name=entity.name,
            email=entity.email.value,
            avatar=entity.avatar,
        )

    def get_users(self) -> List[User]:
        users = UserModel.objects.all()
        # TODO: create model_to_entities
        return list(map(self.model_to_entity, users))

    def get_user_by_id(self, id) -> User:
        user = UserModel.objects.get(id=id)
        # TODO: fetch roles
        return self.model_to_entity(user, [])

    def create(self, user: User) -> None:
        user_model = self.entity_to_model(user)
        user_model.save()
        roles1 = RoleModel.objects.filter(name__in=list(map(lambda r: r.name, user.roles)))
        for role in roles1:
            user_model.roles.add(role)
        # UserRoleModel.objects.create(list(map(lambda r: UserRoleModel())) RoleRepository.entity_to_models(user.roles))

    def update_user(self, user: User) -> None:
        # TODO: update roles
        UserModel.objects.update_or_create(model_to_dict(self.entity_to_model(user)), id=user.id.value)

    # Temp function
    def update_user_avatar(self, user: User) -> None:
        UserModel.objects.filter(id=user.id.value).update(avatar=user.avatar)
