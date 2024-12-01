from django.db import models

# Create your models here.
class Artist(models.Model):
    artistID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Album(models.Model):
    albumID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artistID = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title