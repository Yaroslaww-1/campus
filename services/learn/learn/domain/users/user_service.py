from learn.infrastructure.repositories.user_repository import user_repository


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_users(self):
        users = self.user_repository.get_users()
        return users


user_service = UserService(user_repository)
