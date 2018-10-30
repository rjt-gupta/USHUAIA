from django.contrib import admin

# Register your models here.
from .models import Album, Song, Artist, Playlist

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Playlist)
