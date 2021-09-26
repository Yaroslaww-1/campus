from dataclasses import dataclass


@dataclass
class CreateUserDto:
    name: str
    email: str
