from re import A
from rest_framework.test import APITestCase
from django.urls import reverse 
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "test@example.com",
            "password": "NewPassword@123",
            "password2": "NewPassword@123",

        }