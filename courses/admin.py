from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "level",
        "technology",
        "featured",
        "published",
        "created_at",
    )

    list_filter = (
        "level",
        "featured",
        "published",
    )

    search_fields = (
        "title",
        "technology",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }