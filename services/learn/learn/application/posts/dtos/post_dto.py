import uuid

from dataclasses import dataclass


@dataclass
class PostDto:
    id: uuid.UUID
    name: str
