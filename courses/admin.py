from django.contrib import admin

from .models import *

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



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "order",
        "duration",
        "is_published",
    )

    list_filter = (
        "course",
        "is_published",
    )

    search_fields = (
        "title",
        "course__title",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "course",
        "order",
    )


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "lesson",
        "completed",
        "completed_at",
    )

    list_filter = (
        "completed",
        "lesson__course",
    )

    search_fields = (
        "user__username",
        "user__email",
        "lesson__title",
    )

    ordering = (
        "user",
        "lesson__order",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "certificate_number",
        "user",
        "course",
        "issued_at",
    )

    list_filter = (
        "course",
        "issued_at",
    )

    search_fields = (
        "certificate_number",
        "user__username",
        "user__first_name",
        "user__last_name",
        "course__title",
    )

    readonly_fields = (
        "certificate_number",
        "issued_at",
        "created_at",
    )