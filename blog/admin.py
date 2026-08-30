from django.contrib import admin

from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "published",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "published",
        "created_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-created_at",
    )