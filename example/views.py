import gc
import datetime
from collections import Counter

from django.http import JsonResponse, HttpRequest
from django.conf import settings


def example_view(request: HttpRequest):
    data = {
        'datetime': str(datetime.datetime.now()),
        'path': request.path,
        'objects': len(gc.get_objects()),
        'custom_middleware': settings.USE_CUSTOM,
    }
    return JsonResponse(data)


def middlewares_view(request: HttpRequest):
    return JsonResponse(list(settings.MIDDLEWARE_CLASSES), safe=False)


def garbage_output_view(request: HttpRequest):
    c = Counter(type(o) for o in gc.get_objects() if 'instana' in str(type(o)).lower())
    instana_objects = {str(i): j for i, j in c.most_common(None)}
    gc.collect()
    data = {
        'custom_middleware': settings.USE_CUSTOM,
        'is_enabled': gc.isenabled(),
        'all': len(gc.get_objects()),
        'objects': instana_objects,
    }
    return JsonResponse(data, safe=False)
