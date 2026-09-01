from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "name",
        "is_active",
        "subscribed_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
        "subscribed_at",
    )

    search_fields = (
        "email",
        "name",
    )

    readonly_fields = (
        "subscribed_at",
        "updated_at",
    )

    ordering = (
        "-subscribed_at",
    )