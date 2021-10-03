from pydantic import BaseModel


class StudentGroupDto(BaseModel):
    id: str
    user_id: str
    group_id: str
