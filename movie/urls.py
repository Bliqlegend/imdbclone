from django.contrib import admin
from django.urls import path,include
from .views import MovieViewset,MovieDetailViewset

urlpatterns = [
    path('list/', MovieViewset.as_view()),
    path('list/<int:pk>', MovieDetailViewset.as_view()),
]
