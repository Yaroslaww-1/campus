from learn.domain.posts.events.post_created_domain_event import PostCreatedDomainEvent


class PostCreatedDomainEventHandler:
    def handle(self, event: PostCreatedDomainEvent):
        print(f"PostCreatedDomainEventHandler {event.id.value}")
