from django.contrib import admin
from django.urls import path,include
from .views import MovieViewset,MovieDetailViewset

urlpatterns = [
    path('list/', MovieViewset),
    path('list/<int:pk>', MovieDetailViewset),
]
