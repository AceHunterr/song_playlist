import py_compile
from django.shortcuts import render
from .features.youtube.details import yt_app_details
# Create your views here.

from .forms import YtForm

apps=[
    {
    "slug" : "spotify",
    "image": "language.png",
    "title": "Spotify",
    "colour" : "green",
    "card_no": "card1",
    "features":yt_app_details,
  } ,
  {
    "slug" : "youtube",
    "image": "genre.jpg",
    "title": "Youtube",
    "colour" : "red",
    "card_no": "card2",
    "features":yt_app_details
  },
  {
    "slug" : "reddit",
    "image": "artist.jpg",
    "title": "reddit",
    "colour" : "white",
    "card_no": "card3",
    "features":yt_app_details
  }
]

all_categories = [
  {
    "slug" : "songs-by-language",
    "image": "language.png",
    "title": "Language",
    "colour" : "white",
    "card_no": "card1"
  },
  {
    "slug" : "songs-by-genre",
    "image": "genre.jpg",
    "title": "Genre",
    "colour" : "red",
    "card_no": "card2"
  },
  {
    "slug" : "songs-by-artist",
    "image": "artist.jpg",
    "title": "Artist",
    "colour" : "green",
    "card_no": "card3"
  }
]

songs_list =[
  {
    "slug" : None,
    "image": "song_img1.jpg",
    "name": "Song Title",
    "artist": "Artist 1",
    "genre": "Genre 1",
    "language" : "English"
  },

    {
    "slug" : None,
    "image": "song_img2.jpg",
    "name": "Song Title",
    "artist": "Artist 2",
    "genre": "Genre 2",
    "language" : "English"
  },
    {
    "slug" : None,
    "image": "song_img3.jpg",
    "name": "Song Title",
    "artist": "Artist 1",
    "genre": "Genre 3",
    "language" : "Hindi"
  },
    {
    "slug" : None,
    "image": "artist.jpg",
    "name": "Song Title",
    "artist": "Artist 3",
    "genre": "Genre 2",
    "language" : "Spanish"
  },
    {
    "slug" : None,
    "image": "language.jpg",
    "name": "Song Title",
    "artist": "Artist 2",
    "genre": "Genre 4",
    "language" : "Japanese"
  },
    {
    "slug" : None,
    "image": "song_img3.jpg",
    "name": "Song Title",
    "artist": "Artist 1",
    "genre": "Genre 1",
    "language" : "Hindi"
  },
    {
    "slug" : None,
    "image": "artist.jpg",
    "name": "Song Title",
    "artist": "Artist 4",
    "genre": "Genre 2",
    "language" : "English"
  },
    {
    "slug" : None,
    "image": "artist1.webp",
    "name": "Song Title",
    "artist": "Artist 3",
    "genre": "Genre 2",
    "language" : "Hindi"
  },
    {
    "slug" : None,
    "image": "language1.png",
    "name": "Song Title",
    "artist": "Artist 1",
    "genre": "Genre 1",
    "language" : "English"
  }
]

carousel_list = [
  {
    "id" : "carousel-1",
  },
  {
    "id" : "carousel-2",
  },
  {
    "id" : "carousel-3",
  }
]


def sorting_songs(category,songs_list):
  """Function to sort and make list of songs category wise"""
  cat_items = []
  for song in songs_list:
    for key,value in song.items():
      if key==category:
        if value not in cat_items:
          cat_items.append(value)  

  category_sorting_list = []
  for cat_item in cat_items:
    single_cat_songs = []
    for song in songs_list:
      for key,value in song.items():  
        if key==category and value == cat_item:
          single_cat_songs.append(song)
    category_sorting_list.append({"key":cat_item,"value":single_cat_songs})  

  return category_sorting_list      


songs_list_by_language = sorting_songs("language",songs_list)
songs_list_by_genre = sorting_songs("genre",songs_list)
songs_list_by_artist = sorting_songs("artist",songs_list)

# for song in songs_list:
#   for key,value in song.items():
#     if key=="artist":
#       if value not in artists:
#         artists.append(value)

# for artist in artists:
#   single_artist_songs = []
#   for song in songs_list:
#     for key,value in song.items():  
#       if key=="artist" and value == artist:
#         single_artist_songs.append(song)
#   songs_list_by_artist.append({artist:single_artist_songs})


def index(request):
  return render(request , "songs/index.html",{
    "apps" : apps
  })

def spotify(request):
  return render(request,"songs/spotify.html",{
    "features" : apps[0]["features"],
    "form" : YtForm
    }
  )

def youtube(request):
  return render(request,"songs/youtube.html",{
    "features" : apps[1]["features"],
    "form" : YtForm
    }
  )

def reddit(request):
  return render(request,"songs/reddit.html",{
    "features" : apps[2]["features"],
    "form" : YtForm
    }
  )

def yt_input(request):
  return render(request,"songs/yt_input.html",{
    'var' : "hello"
  })


def category_sorted_page(request):
  return render(request , "songs/category_sorted.html",{
    "all_categories" : all_categories
  })

def songs_by_language(request):
  return render(request, "songs/songs_by_language.html",{
  "sorted_list":songs_list_by_language}
  )

def songs_by_genre(request):
  return render(request, "songs/songs_by_genre.html",{
    "sorted_list":songs_list_by_genre
  })

def songs_by_artist(request):
  return render(request, "songs/songs_by_artist.html",{
  "sorted_list" : songs_list_by_artist}
  )

def all_songs(request):
  return render(request, "songs/all_songs.html",{
    "songs_list" : songs_list,
    "carousel_list" : carousel_list
  })