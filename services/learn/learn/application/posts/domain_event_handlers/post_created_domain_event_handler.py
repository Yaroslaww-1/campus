import inject

from learn.domain.posts.events.post_created_domain_event import PostCreatedDomainEvent
from learn.infrastructure.repositories.student_repository import StudentRepository


class PostCreatedDomainEventHandler:
    @inject.autoparams()
    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def handle(self, event: PostCreatedDomainEvent):
        print(f"PostCreatedDomainEventHandler {event.id.value} len: {len(self.repo.get_students())}")
