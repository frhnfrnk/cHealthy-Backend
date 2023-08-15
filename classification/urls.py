from django.urls import path

from . import api

urlpatterns = [
    path('predict', api.predict, name='predict'),
]