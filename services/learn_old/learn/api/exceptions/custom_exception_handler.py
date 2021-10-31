import logging

from pydantic import ValidationError
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist


def custom_exception_handler(ex, context):
    logging.log(logging.ERROR, f'Exception occurred: {repr(ex)}')
    if isinstance(ex, ObjectDoesNotExist):
        err_data = {'message': 'Object Does Not Exist'}
        return Response(err_data, status=status.HTTP_404_NOT_FOUND)
    if isinstance(ex, ValidationError):
        err_data = {'message': 'Validation Error', 'details': ex.errors()}
        return Response(err_data, status=status.HTTP_400_BAD_REQUEST)
    if isinstance(ex, PermissionDenied):
        err_data = {'message': 'Permission Error'}
        return Response(err_data, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Unhandled Error', 'details': ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
