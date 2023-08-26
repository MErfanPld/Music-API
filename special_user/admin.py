from django.contrib import admin
from .models import Special, PlanMusic

# Register your models here.


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ["user", "plan_music","expires_at"]
    readonly_fields = ["created_at"]


@admin.register(PlanMusic)
class PlanMusicAdmin(admin.ModelAdmin):
    list_display = ["title", "time_months", "price"]
