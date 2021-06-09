from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('login/', obtain_auth_token, name='login')
]