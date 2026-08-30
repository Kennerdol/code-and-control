from django.db import models
from django.urls import reverse


class BlogCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )

    excerpt = models.TextField(
        max_length=500
    )

    content = models.TextField()

    featured_image = models.ImageField(
        upload_to="blog/",
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
            "blog_detail",
            kwargs={"slug": self.slug}
        )