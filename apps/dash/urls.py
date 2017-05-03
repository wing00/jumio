from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'hello', hello),
    url(r'jumio_webhook', jumio_webhook)
]