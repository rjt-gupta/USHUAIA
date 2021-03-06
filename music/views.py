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


def artist_detail(request):
	all_artist = Artist.objects.all()
	context = {
		'all_artist': all_artist
	}
	return render(request, 'music/artist.html', context)


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


def add_to_playlist(request):

	form = PlaylistForm(request.POST or None)

	if form.is_valid():

		data = form.cleaned_data
		new_play = Playlist.objects.create()
		new_play.play_name = data['play_name']

		new_play.save()

	context = {
		"form": form
	}
	return render(request, 'music/add_to_playlist.html', context)


def delete_song(request, song_id):

	song = Song.objects.get(pk=song_id)
	print(song.song_title)
	song.delete()

	return HttpResponse("Deleted Successfully")


def delete_song_playlist(request, play_id):

	playlist = Playlist.objects.get(pk=play_id)
	print(playlist.play_name)
	playlist.delete()

	return HttpResponse("Success")


def delete_album(request, album_id):

	album = Album.objects.get(pk=album_id)
	print(album)
	album.delete()

	return HttpResponse("Album Deleted..")


def delete_artist(request, artist_id):

	artist = Artist.objects.get(pk=artist_id)
	print(artist)
	artist.delete()

	return HttpResponse("Artist Removed from Library..")


"""
from django.views import generic
# By Default Django has generic views to make such things easier and a lot faster

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'  # To change default object_list to our variable name

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
"""
