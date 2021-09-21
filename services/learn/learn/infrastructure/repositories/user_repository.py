from learn.models import User


class UserRepository:
    def __init__(self):
        pass

    def get_users(self):
        return User.objects.all()


user_repository = UserRepository()
