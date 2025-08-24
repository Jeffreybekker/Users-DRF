from rest_framework import serializers
from .models import Artist, Album


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artistID", "first_name", "last_name"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["albumID", "title", "artistID"]
