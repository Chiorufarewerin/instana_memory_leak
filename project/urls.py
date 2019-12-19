from django.conf.urls import url
from django.contrib import admin
from example.views import example_view, garbage_output_view, middlewares_view

urlpatterns = [
    url(r'^middleware/*?$', middlewares_view),
    url(r'^gc/*?$', garbage_output_view),
    url(r'^.*$', example_view),
]
