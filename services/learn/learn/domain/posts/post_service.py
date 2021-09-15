from learn.infrastructure.repositories.post_repository import post_repository


class PostService:
    def __init__(self, post_repository):
        self.post_repository = post_repository

    def get_posts(self):
        posts = self.post_repository.get_posts()
        return posts


post_service = PostService(post_repository)
