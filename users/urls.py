from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from users.views import *

urlpatterns = [
    path('login/', user_login),
    path('register/', user_register),
    path('stkstatus/', get_stkstatus),
]
