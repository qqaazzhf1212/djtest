from django.urls import path
from djapp.views import index


urlpatterns=[
    path('index/', index),
]