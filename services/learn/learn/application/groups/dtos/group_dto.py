from pydantic import BaseModel


class GroupDto(BaseModel):
    id: str
    name: str
    formed_at_year: int
