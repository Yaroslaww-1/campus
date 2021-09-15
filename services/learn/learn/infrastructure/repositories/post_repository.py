from learn.domain.posts.entities.post import Post


class PostRepository:
    # TODO: inject SQLConnection here
    def __init__(self):
        pass

    def get_posts(self):
        posts = [Post("1", "Dopka is coming!"), Post("2", "Dopka is cancelled!")]
        return posts


post_repository = PostRepository()
