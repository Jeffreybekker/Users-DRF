from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=100, default="Netherlands")
    city = models.CharField(max_length=100, default="Unknown")
    
    def __str__(self):
        return self.name