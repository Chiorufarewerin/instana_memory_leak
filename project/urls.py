from django.conf.urls import url
from example.views import example_view, garbage_output_view, middlewares_view, trace_start, trace

urlpatterns = [
    url(r'^middleware/*?$', middlewares_view),
    url(r'^gc/*?$', garbage_output_view),
    url(r'^start.*', trace_start),
    url(r'^trace.*', trace),
    url(r'^.*$', example_view),
]
