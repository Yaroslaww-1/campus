from learn.models import Post


class PostRepository:
    def __init__(self):
        pass

    def get_all_posts(self):
        return Post.objects.all()

    def get_post_by_id(self, id):
        return Post.objects.get(id=id)

    def get_post_by_name(self, name):
        return Post.objects.get(name=name)

    def create_post(self, id, name):
        Post.objects.create(id=id, name=name)

    def delete_post_by_id(self, id):
        Post.objects.filter(id=id).delete()

    def delete_post_by_name(self, name):
        Post.objects.filter(name=name).delete()


post_repository = PostRepository()
