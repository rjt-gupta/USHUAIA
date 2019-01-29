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


def song_detail(request, album_id):
	album = Album.objects.get(pk=album_id)
	context = {
		'album': album
	}
	return render(request, 'music/detail.html', context)

def playlist_detail(request):
	all_playlist = Playlist.objects.all()
	count = all_playlist.count()
	context = {
		'all_playlist': all_playlist,
		'count': count
	}
	return render(request, 'music/playlist.html', context)

def create_artist(request):

	form = ArtistForm(request.POST or None)

	if form.is_valid():
		data = form.cleaned_data
		artist = Artist.objects.create()
		artist.name = data['name']
		artist.screen_name = data['screen_name']

		artist.save()

	context = {
		"form": form,
	}
	return render(request, 'music/create_artist.html', context)

def create_album(request, artist_id):

	form = AlbumForm(request.POST or None)

	if form.is_valid():

		data = form.cleaned_data
		artist = Artist.objects.get(pk=artist_id)
		album = artist.album_set.create()
		album.album_title = data['album_title']
		album.artist_name = data['artist_name']

		album.save()
	context = {
		"form": form
	}

	return render(request, 'music/create_album.html', context)

def create_song(request, album_id):

	form = SongForm(request.POST or None)

	if form.is_valid():

		data = form.cleaned_data
		album = Album.objects.get(pk=album_id)
		song = album.song_set.create()
		song.song_title = data['song_title']

		song.save()

	context = {
		"form": form
	}

	return render(request, 'music/create_song.html', context)

