from learn.models import User


class UserRepository:
    def __init__(self):
        pass

    def get_users(self):
        return User.objects.all()

    def get_user_by_id(self, id):
        return User.objects.get(id=id)


user_repository = UserRepository()
