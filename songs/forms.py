from socket import fromshare
from django import forms
from .models import Yt

class YtForm(forms.ModelForm):
    class Meta:
        model = Yt
        fields = '__all__'
        labels ={
            "pl_link" : "Playlist Link",
            "country" : "Region/Country",
            "date" : "Date(In Format : mm/dd/yyyy)",
            "search": "Search Word"
        }