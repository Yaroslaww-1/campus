from learn.models import User


class UserRepository:
    def __init__(self):
        pass

    def get_users(self):
        return User.objects.all()

    def get_user_by_id(self, id):
        return User.objects.get(id=id)

    def create_user(self, id, name, email):
        User.objects.create(id=id, name=name, email=email)
        return User.objects.get(id=id)

    def update_user(self, id, name, email):
        User.objects.filter(id=id).update(name=name, email=email)
        return User.objects.get(id=id)

    def delete_user_by_id(self, id):
        User.objects.filter(id=id).delete()


user_repository = UserRepository()
