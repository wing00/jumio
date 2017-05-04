from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^logs/(?P<path>.*)$', serve,
        {'document_root': '/django/logs',
         'show_indexes': True}),
    url(r'jumio_webhook', jumio_webhook),
]
