import inject

from learn.infrastructure.repositories.post_repository import PostRepository


class InfrastructureModule:
    def load(self):
        self.load_di()

    def load_di(self):
        def di_configuration(binder):
            binder.bind(PostRepository, PostRepository())
        inject.configure(di_configuration)
