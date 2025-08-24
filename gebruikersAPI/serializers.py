# serializers.py
from rest_framework import serializers

from .models import Album, Artist


# Output serializer (wat de client ziet)
class ArtistOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["artistID", "first_name", "last_name"]

class ArtistInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["first_name", "last_name"]  # client mag geen artistID sturen

class AlbumOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["albumID", "title", "artistID"]

class AlbumInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["title", "artistID"]  # client mag geen albumID sturen
