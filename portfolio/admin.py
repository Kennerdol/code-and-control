from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project_type",
        "status",
        "featured",
        "created_at",
    )

    list_filter = (
        "project_type",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "short_description",
        "technologies",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-created_at",
    )