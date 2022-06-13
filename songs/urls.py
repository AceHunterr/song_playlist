from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("songs-by-language",views.songs_by_language,name="songs-by-language"),
    path("songs-by-genre",views.songs_by_genre,name="songs-by-genre"),
    path("songs-by-artist",views.songs_by_artist,name="songs-by-artist"),
]
