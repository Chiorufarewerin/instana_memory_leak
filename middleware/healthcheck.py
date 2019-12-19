from django.http import HttpRequest, HttpResponse, JsonResponse
from instana.instrumentation.django.middleware import InstanaMiddleware as _InstanaMiddleware


class HealthCheckMiddleware:
    """This middleware must be first"""

    def process_request(self, request: HttpRequest):
        request.is_healthcheck = False
        if request.method == 'GET' and request.path.rstrip('/') == '/healthcheck':
            request.is_healthcheck = True
            return JsonResponse({'status': 'OK'})


class HealthCheckBase:
    """Middlewares will works without process response"""

    def process_response(self, request: HttpRequest, response: HttpResponse):
        if request.is_healthcheck:
            return response
        return super().process_response(request, response)


class InstanaMiddleware(HealthCheckBase, _InstanaMiddleware):
    pass
