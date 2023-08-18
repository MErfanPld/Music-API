from django.contrib import admin
from .models import Album
from django.utils.html import format_html

# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "user","likeCount", "viewCount",
                    "playCount", "status", "image_tag", "created_at", "updated_at"]
    readonly_fields = ['created_at', 'updated_at',
                       'likeCount', 'viewCount', 'playCount']

    def image_tag(self, obj):
        if obj.cover:
            img = obj.cover.url
            return format_html('<img src="{}" width=50 />'.format(img))
        return None

    image_tag.short_description = 'Album Cover'
