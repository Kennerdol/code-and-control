from django.db import models
from django.urls import reverse

from portfolio.models import Project
from resources.models import Resource


class Post(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("automation", "Automation"),
        ("embedded", "Embedded Systems"),
        ("data", "Data & Analytics"),
        ("career", "Career"),
        ("tutorial", "Tutorial"),
        ("other", "Other"),
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

    excerpt = models.CharField(
        max_length=300
    )

    content = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    featured_image = models.ImageField(
        upload_to="blog/",
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

    author = models.CharField(
        max_length=100,
        default="Code & Control"
    )

    related_project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="blog_posts"
    )

    related_resources = models.ManyToManyField(
        Resource,
        blank=True,
        related_name="blog_posts"
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
            "post_detail",
            kwargs={
                "slug": self.slug
            }
        )