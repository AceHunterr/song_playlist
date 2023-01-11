from django.urls import is_valid_path , reverse
import py_compile
from .features.youtube.details import yt_app_details
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

# Create your views here.

from .forms import YtForm

apps=[
    {
    "slug" : "spotify",
    "image": "spotify.png",
    "title": "Spotify",
    "colour" : "green",
    "card_no": "card1",
    "features":yt_app_details,
  } ,
  {
    "slug" : "youtube",
    "image": "youtube.png",
    "title": "Youtube",
    "colour" : "red",
    "card_no": "card2",
    "features":yt_app_details
  },
  {
    "slug" : "reddit",
    "image": "reddit.png",
    "title": "Reddit",
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
    "image": "genre.png",
    "title": "Genre",
    "colour" : "red",
    "card_no": "card2"
  },
  {
    "slug" : "songs-by-artist",
    "image": "artist.png",
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


class YoutubeView(View):

  def feature_result(self,data):
    for items in yt_app_details:
      if items["value"]["feature_no"] == data["feature_no"]:
        feat_function = items["value"]["function"]
    
    data.popitem()
    # for (key,value) in data: 
    #   pass
    return feat_function(**data)
  
  def list_pair(self,list):
    new_list = []

    for i in range(int(0.5*len(list))):

      temp_list = []
      for j in range(2):
        temp_list.append(list[(2*i)+j])
      
      new_list.append(temp_list)

    return new_list

  def get(self,request):
    context = {
      "features" : apps[1]["features"],
      "form" : YtForm 
    }
    return render(request,"songs/youtube.html",context)
  
  def post(self,request):
    input_form = YtForm(request.POST)
    if input_form.is_valid():
      input_form.save()
    data = input_form.cleaned_data
    result = self.feature_result(data)

    
    if type(result) == str:
      result_data_type = "string"
    else:
      result_data_type = "list"
    # return HttpResponseRedirect(reverse("yt_results"),args=[input_form])

    return render(request, "songs/yt_results.html",{
      "data": data,
      "result" : result,
      "result_data_type" : result_data_type,
      "paired_result" : self.list_pair(result)
    })
    # return HttpResponseRedirect(reverse("yt_results"))
      
               
                    


def reddit(request):

  return render(request,"songs/reddit.html",{   
    "features" : apps[2]["features"],
    "form" : YtForm
    }
  )
  


def yt_results(request):
  return render(request,"songs/yt_results.html",{
    
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

class SavedView(View):
  def get(self,request):
    pass
  def post(self,request):
    pass


class SavedView(View):
  def get(self,request):
    saved = request.session.get("saved")
    context ={}

    if stored_posts is None or len(stored_posts) == 0:
      context["posts"] = []
      context["has_posts"] = False
    else:
      posts = Post.objects.filter(id__in=stored_posts)
      context["posts"] = posts
      context["has_posts"] = True

    return render(request, "blog/stored-posts.html",context)


  def post(self,request):
    stored_posts = request.session.get("stored_posts")

    if stored_posts is None:
      stored_posts = [] 

    post_id = int(request.POST["post_id"])

    if post_id not in stored_posts:
      stored_posts.append(post_id)
    else:
      stored_posts.remove(post_id)
    request.session["stored_posts"] = stored_posts
    
    return HttpResponseRedirect("/")