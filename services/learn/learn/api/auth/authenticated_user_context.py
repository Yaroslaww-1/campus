import uuid

from django.core.exceptions import BadRequest
from django.http import HttpRequest

from learn.domain.users.value_objects.user_id import UserId


class AuthenticatedUserContext:
    def __init__(self, request: HttpRequest):
        self.request = request

    @property
    def user_id(self) -> UserId:
        user_id = self.request.headers['Userid']
        if not user_id:
            raise BadRequest("Request is authenticated but user id is missing.")
        return UserId(uuid.UUID(user_id))
