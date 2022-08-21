from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
  list_filter = ("artist","genre","language",)
  list_display = ("name","artist")
  prepopulated_fields = {"slug": ("name",)}
  
admin.site.register(Song,SongAdmin)
# Register your models here.
 