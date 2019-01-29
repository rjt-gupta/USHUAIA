from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Artist, Playlist


class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ['name', 'screen_name']


class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['artist_name', 'album_title']


class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['song_title']


class PlaylistForm(forms.ModelForm):
	class Meta:

		model = Playlist
		fields = ['play_name']

