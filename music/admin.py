from django.contrib import admin
from .models import Music
from django.utils.html import format_html

# Register your models here.


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "singer", "is_special_music", "likeCount", "viewCount",
                    "playCount", "status", "image_tag", "created_at", "updated_at"]
    readonly_fields = ['likeCount', 'viewCount', 'playCount']

    def image_tag(self, obj):
        if obj.cover:
            img = obj.cover.url
            return format_html('<img src="{}" width=50 />'.format(img))
        return None

    image_tag.short_description = 'Music Cover'
