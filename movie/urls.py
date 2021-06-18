from django.contrib import admin
from django.urls import path,include
from .views import (MovieViewset,MovieDetailViewset,
                StreamPlatformViewset,SpdetailViewset,
                ReviewViewset,ReviewDetailViewset,ReviewCreateViewset,
                UpcomingViewset,GenreViewset,UserReView)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'upcoming',UpcomingViewset,basename='upcoming')
router.register(r'genre',GenreViewset,basename='genre')

urlpatterns = [
    path('list/', MovieViewset.as_view(), name='movie-lsit'),
    path('list/<int:pk>', MovieDetailViewset.as_view(),name='movie-detail'),
    path('platform/',StreamPlatformViewset.as_view(),name='stream-platform'),
    path('platform/<int:pk>', SpdetailViewset.as_view(),name='streamplatforms-detail'),
    path('review/<int:pk>/',ReviewDetailViewset.as_view(),name='review-detail'),
    path('review/<int:pk>/create/',ReviewCreateViewset.as_view(),name='review-create'),
    path('review/', ReviewViewset.as_view(),name='review'),
    path('review/<str:username>/',UserReView.as_view(),name='user-review'),
    path('',include(router.urls)),
]