from django.contrib import admin
from .models import Playlist

# Register your models here.


@admin.register(Playlist)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "image", "status"]
