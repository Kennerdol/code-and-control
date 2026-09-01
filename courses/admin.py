from django.contrib import admin

from .models import Course, Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "level",
        "duration",
        "status",
        "featured",
        "created_at",
    )

    list_filter = (
        "level",
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


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "course",
        "user",
        "status",
        "enrolled_at",
    )

    list_filter = (
        "status",
        "course",
        "enrolled_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "user__username",
        "user__email",
        "course__title",
    )

    readonly_fields = (
        "enrolled_at",
        "updated_at",
    )

    ordering = (
        "-enrolled_at",
    )