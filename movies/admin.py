from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "protagonists", "ranking"]
    list_filter = ["status"]
    search_fields = [
        "name",
    ]
    list_per_page = 10
    ordering = ["id"]
