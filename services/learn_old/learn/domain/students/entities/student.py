from learn.domain.groups.entities.group import Group
from learn.domain.users.entities.user import User


class Student:
    def __init__(self, user: User, group: Group):
        self.user = user
        self.group = group
