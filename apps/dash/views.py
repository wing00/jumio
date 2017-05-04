from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse, QueryDict
import logging

logger = logging.getLogger('testlogger')


def hello(request):
    return JsonResponse({"hello": "world"}, status=status.HTTP_200_OK)


def jumio_webhook(request):
    result = QueryDict(request.body)

    logger.info({"raw": request,
                 "raw.body": request.body,
                 "result": result,
                 })

    return JsonResponse(result, status=status.HTTP_200_OK)
