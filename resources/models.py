from django.db import models
from django.urls import reverse


class Resource(models.Model):

    CATEGORY_CHOICES = [
        ("tutorial", "Tutorial"),
        ("guide", "Guide"),
        ("cheatsheet", "Cheat Sheet"),
        ("ebook", "eBook"),
        ("code", "Source Code"),
        ("template", "Template"),
        ("other", "Other"),
    ]

    TYPE_CHOICES = [
        ("article", "Article"),
        ("pdf", "PDF"),
        ("code", "Code"),
        ("video", "Video"),
        ("external", "External Link"),
    ]

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    resource_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    file = models.FileField(
        upload_to="resources/",
        blank=True,
        null=True
    )

    external_url = models.URLField(
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="resources/images/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "resource_detail",
            kwargs={"slug": self.slug}
        )