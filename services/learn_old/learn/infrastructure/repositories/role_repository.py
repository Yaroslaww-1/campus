from typing import List

from learn.domain.users.entities.role import Role
from learn.domain.users.value_objects.role_id import RoleId
from learn.models import Role as RoleModel


class RoleRepository:
    @staticmethod
    def model_to_entity(model: RoleModel) -> Role:
        return Role(
            id=RoleId(model.id),
            name=model.name,
        )

    @staticmethod
    def model_to_entities(models: List[RoleModel]) -> List[Role]:
        return list(map(lambda r: RoleRepository.model_to_entity(r), models))

    @staticmethod
    def entity_to_model(entity: Role) -> RoleModel:
        return RoleModel(
            id=entity.id.value,
            name=entity.name,
        )

    @staticmethod
    def entity_to_models(entities: List[Role]) -> List[RoleModel]:
        return list(map(lambda r: RoleRepository.entity_to_model(r), entities))

    def get_roles(self) -> List[Role]:
        roles = RoleModel.objects.all()
        return list(map(self.model_to_entity, roles))
