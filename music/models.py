from django.db import models


class Artist(models.Model):
	name = models.CharField(max_length=20)
	screen_name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Album(models.Model):
	album_title = models.CharField(max_length=20)
	artist_name = models.CharField(max_length=20)
	genre_desc = models.CharField(max_length=100, default="")
	artistfk = models.ForeignKey(Artist, on_delete=models.CASCADE)

	def __str__(self):
		return self.album_title


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	extension = models.CharField(max_length=10)
	song_title = models.CharField(max_length=20)

	def __str__(self):
		return self.song_title


class Playlist(models.Model):
	play_name = models.CharField(max_length=20)
	track = models.IntegerField(max_length=None, default=0)
	song = models.ForeignKey(Song, on_delete=models.CASCADE, default="22")


