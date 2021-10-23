import json
from functools import wraps, partial
from typing import List

from rest_framework.exceptions import PermissionDenied

from learn.api.enums.roles_enum import Role


def in_roles(roles: List[Role]):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            roles_from_request = json.loads(request.headers['Userroles'])
            role_from_request = roles_from_request['Name']
            for role in roles:
                if role_from_request == str(role.value):
                    return function(request, *args, **kwargs)
            raise PermissionDenied("Permission denied")
        return wrap
    return decorator
