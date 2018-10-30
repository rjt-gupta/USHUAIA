from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from music.views import album_detail, song_detail, artist_detail, playlist_detail, create_artist, create_album, create_song, add_to_playlist, delete_song
from music.views import delete_song_playlist, delete_album, delete_artist
urlpatterns = [
	path('admin/', admin.site.urls),
	# path('music/',views.IndexView.as_view()),  # generic way
	# path('music/' + '<int:pk>/', views.DetailView.as_view())
	path('music/', artist_detail),  # use this if you use the easy way
	path('music/songs/' + '<int:album_id>', song_detail),  # In django 2.0 regular expressions can be used by re_path()
	path('music/album/' + '<int:artist_id>', album_detail),
	path('music/playlist', playlist_detail),
	path('music/create_artist', create_artist),
	path('music/create_album/' + '<int:artist_id>', create_album),
	path('music/create_song/' + '<int:album_id>', create_song),
	path('music/add_to_playlist/', add_to_playlist),
	path('music/delete_song/' + '<int:song_id>', delete_song),
	path('music/delete_song_playlist/' + '<int:play_id>', delete_song_playlist),
	path('music/delete_album/' + '<int:album_id>', delete_album),
	path('music/delete_artist/' + '<int:artist_id>', delete_artist)

]
