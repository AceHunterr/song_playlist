from django.shortcuts import render

# Create your views here.

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

def index(request):
  return render(request , "songs/index.html",{
    "all_categories" : all_categories
  })

def songs_by_language(request):
  return render(request, "songs/songs_by_language.html")

def songs_by_genre(request):
  return render(request, "songs/songs_by_genre.html")

def songs_by_artist(request):
  return render(request, "songs/songs_by_artist.html")

def all_songs(request):
  return render(request, "songs/all_songs.html")