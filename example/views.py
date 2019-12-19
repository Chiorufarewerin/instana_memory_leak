import gc
import datetime

from django.http import JsonResponse, HttpRequest


def example_view(request: HttpRequest):
    data = {
        'datetime': str(datetime.datetime.now()),
        'path': request.path,
    }
    return JsonResponse(data)
