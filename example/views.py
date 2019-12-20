import gc
import datetime
import tracemalloc
from collections import Counter

from django.http import JsonResponse, HttpRequest
from django.conf import settings


check = None


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
    gc.collect()
    c = Counter(type(o) for o in gc.get_objects() if 'instana' in str(type(o)).lower())
    instana_objects = {str(i): j for i, j in c.most_common(None)}
    data = {
        'custom_middleware': settings.USE_CUSTOM,
        'is_enabled': gc.isenabled(),
        'all': len(gc.get_objects()),
        'objects': instana_objects,
    }
    return JsonResponse(data, safe=False)


def trace_start(request: HttpRequest):
    tracemalloc.start()
    return JsonResponse({}, safe=False)


def trace(request: HttpRequest):
    gc.collect()
    global check
    snapshot = tracemalloc.take_snapshot()
    tracemalloc.get_tracemalloc_memory()
    statistics = list(filter(lambda s: 'tracemalloc' not in str(s.traceback),
                      sorted(snapshot.statistics('lineno'), key=lambda s: s.count, reverse=True)))
    statistic = {str(s.traceback): s.count for s in statistics}
    if check is None:
        check = statistic
        data = {}
    else:
        temp = statistic.copy()
        for key, val in statistic.items():
            count = check.pop(key, 0)
            if val - count:
                check[key] = val - count
        data = check
        check = temp
    checks = [
        'trace',
    ]
    objects = []
    for s in statistics:
        s = str(s)
        for ch in checks:
            if ch in s:
                objects.append(s)
    mem1, mem2 = tracemalloc.get_traced_memory()
    top = list(map(str, statistics[:10]))
    return JsonResponse(dict(mem1=mem1, mem2=mem2, top=top, objects=objects, data=data), safe=False)


# tracemalloc.start()
# gc.disable()
