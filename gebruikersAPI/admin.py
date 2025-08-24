from django.contrib import admin

from .models import Album, Artist, Genre, Track

# Register your models here.
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
