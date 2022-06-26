from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  # list_filter = ("artist")
admin.site.register(Song,SongAdmin)
# Register your models here.
