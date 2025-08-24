# urls.py
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, ArtistViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = router.urls
