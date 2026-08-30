from django.contrib import admin

from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "resource_type",
        "status",
        "featured",
        "created_at",
    )

    list_filter = (
        "category",
        "resource_type",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-created_at",
    )