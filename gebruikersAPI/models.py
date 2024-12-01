from django.db import models

# Create your models here.
class Artist(models.Model):
    artistID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)