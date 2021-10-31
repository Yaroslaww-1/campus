import uuid


from learn.domain.users.value_objects.role_id import RoleId


# IMPORTANT: this class is temporary. It should be replaced with enum value object
class Role:
    def __init__(self, id: RoleId, name: str):
        self.id = id
        self.name = name

    @classmethod
    def create_new_role(cls, name: str) -> "Role":
        id = RoleId(value=uuid.uuid4())
        role = Role(id, name)
        return role

    @classmethod
    def initialize(cls, id: RoleId, name: str) -> "Role":
        role = Role(id, name)
        return role
