from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreamingPlatformViewSet, GenreViewSet, MovieViewSet, recommend_movie

router = DefaultRouter()
router.register(r'streams', StreamingPlatformViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', recommend_movie, name='recommend-movie'),
]
