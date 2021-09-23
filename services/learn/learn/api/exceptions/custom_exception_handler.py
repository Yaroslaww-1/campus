import logging

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist


def custom_exception_handler(exc, context):
    err_data = {exc.args}
    if isinstance(exc, ObjectDoesNotExist):
        err_data = {'Object Does Not Exist'}
        return Response(err_data, status=status.HTTP_404_NOT_FOUND)
    return Response(err_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
