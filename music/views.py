from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .forms import ArtistForm, AlbumForm, SongForm, PlaylistForm
from .models import Album, Song, Artist, Playlist
from django.shortcuts import render


# This is the easy way to do things manually to understand the concept ::::


def album_detail(request, artist_id):
	artist = Artist.objects.get(pk=artist_id)
	all_albums = Album.objects.all()
	context = {
		'all_albums': all_albums,
		'artist': artist

	}
	return render(request, 'music/album.html', context)