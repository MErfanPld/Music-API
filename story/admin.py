from django.contrib import admin
from .models import Story
from django.utils.html import format_html

# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "updated_at"]
    readonly_fields = ['created_at', 'updated_at']
