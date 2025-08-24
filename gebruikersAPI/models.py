from django.db import models


class Artist(models.Model):
    artistID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)  # Artist first name
    last_name = models.CharField(max_length=100)  # Artist last name

    def __str__(self):
        return self.first_name + " " + self.last_name  # Gives the Artists full name


class Album(models.Model):
    albumID = models.AutoField(primary_key=True)  # ID for the Album
    title = models.CharField(max_length=100)  # Name of the album
    artistID = models.ForeignKey(
        Artist, on_delete=models.CASCADE
    )  # When you delete an artistID, Album will be deleted too

    def __str__(self):
        # Gives the Album name + full name of artist
        return f"{self.title} ({self.artistID.first_name} {self.artistID.last_name})"


class Genre(models.Model):
    GenreID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Track(models.Model):
    trackID = models.AutoField(primary_key=True)  # ID of the track
    name = models.CharField(max_length=100)  # Name of the track
    albumID = models.ForeignKey(
        Album, on_delete=models.CASCADE
    )  # When you delete an Album, the Track will be deleted too
    genreID = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True
    )  # When you delete a Genre, it'll SET NULL for genre in Track

    def __str__(self):
        return self.name
