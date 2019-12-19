from django.conf.urls import url
from django.contrib import admin
from example.views import example_view

urlpatterns = [
    url(r'^.*$', example_view)
]
