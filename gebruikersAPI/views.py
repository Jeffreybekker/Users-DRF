from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer


# GET and POST for users
@api_view(["GET", "POST"])
def artist_list(request):
    if request.method == "GET":
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET, POST, DELETE for a single user
@api_view(["GET", "PUT", "DELETE"])
def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET and POST for albums
@api_view(["GET", "POST"])
def album_list(request):
    if request.method == "GET":
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get, PUT, DELETE albums from an artist
@api_view(["GET", "PUT", "DELETE"])
def album_detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
