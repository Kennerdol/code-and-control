from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "featured",
        "related_project",
        "author",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "author",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "related_resources",
    )

    ordering = (
        "-created_at",
    )