from django.contrib import admin
from django.urls import path,include
from .views import MovieViewset,MovieDetailViewset,StreamPlatformViewset,SpdetailViewset

urlpatterns = [
    path('list/', MovieViewset.as_view(), name='movie-lsit'),
    path('list/<int:pk>', MovieDetailViewset.as_view(),name='movie-detail'),
    path('platform/',StreamPlatformViewset.as_view(),name='stream-platform'),
    path('platform/<int:pk>', SpdetailViewset.as_view(),name='streamplatforms-detail')
]
