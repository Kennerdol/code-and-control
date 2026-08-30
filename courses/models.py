from django.db import models
from django.urls import reverse


class Course(models.Model):

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField(
        max_length=300
    )

    description = models.TextField()

    instructor = models.CharField(
        max_length=150,
        default="Code & Control"
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner"
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    technology = models.CharField(
        max_length=200,
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    featured = models.BooleanField(
        default=False
    )

    published = models.BooleanField(
        default=True
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
            "course_detail",
            kwargs={"slug": self.slug}
        )