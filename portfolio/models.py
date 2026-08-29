from django.db import models
from django.urls import reverse


class Project(models.Model):

    PROJECT_TYPES = [
        ("web", "Web Application"),
        ("mobile", "Mobile Application"),
        ("desktop", "Desktop Application"),
        ("automation", "Automation"),
        ("data", "Data & Analytics"),
        ("embedded", "Embedded System"),
        ("other", "Other"),
    ]

    PROJECT_STATUS = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("archived", "Archived"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Example: Django, PostgreSQL, HTML, CSS"
    )

    featured_image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default="in_progress",
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
            "project_detail",
            kwargs={"slug": self.slug}
        )