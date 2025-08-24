from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Album, Artist
from .serializers import (
    AlbumInputSerializer,
    AlbumOutputSerializer,
    ArtistInputSerializer,
    ArtistOutputSerializer,
)


@extend_schema(tags=['Artists'])
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistOutputSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ArtistInputSerializer
        return ArtistOutputSerializer

    def destroy(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return Response({"detail": "DELETE on list not allowed"}, status=405)
        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=['Albums'])
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumOutputSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AlbumInputSerializer
        return AlbumOutputSerializer

    def destroy(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return Response({"detail": "DELETE on list not allowed"}, status=405)
        return super().destroy(request, *args, **kwargs)
