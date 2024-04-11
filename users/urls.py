from django.conf.urls import url
from django.urls import path

from users.views import user_login,user_register

urlpatterns = [
    path('login/', user_login),
    path('register/', user_register),
]

