from django.db import models


class Subscriber(models.Model):

    email = models.EmailField(
        unique=True
    )

    name = models.CharField(
        max_length=100,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-subscribed_at"]

    def __str__(self):
        return self.email