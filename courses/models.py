import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
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

    curriculum = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
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

    instructor = models.CharField(
        max_length=100,
        default="Code & Control"
    )

    featured_image = models.ImageField(
        upload_to="courses/",
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
            "course_detail",
            kwargs={
                "slug": self.slug
            }
        )



class Enrollment(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="course_enrollments",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.name} - {self.course.title}"



class Lesson(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220
    )

    description = models.TextField(
        blank=True
    )

    content = models.TextField()

    order = models.PositiveIntegerField(
        default=1
    )

    video_url = models.URLField(
        blank=True
    )

    duration = models.CharField(
        max_length=50,
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order"]

        constraints = [
            models.UniqueConstraint(
                fields=["course", "slug"],
                name="unique_lesson_slug_per_course"
            )
        ]

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "lesson_detail",
            kwargs={
                "course_slug": self.course.slug,
                "slug": self.slug,
            }
        )



class LessonProgress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lesson_progress"
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="progress_records"
    )

    completed = models.BooleanField(
        default=False
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["lesson__order"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "lesson"],
                name="unique_user_lesson_progress"
            )
        ]

    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.lesson.title}"
        )


class Certificate(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    certificate_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False
    )

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-issued_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "course"],
                name="unique_user_course_certificate"
            )
        ]

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.course.title}"
        )

    def save(self, *args, **kwargs):

        if not self.certificate_number:

            self.certificate_number = (
                f"CC-{uuid.uuid4().hex[:10].upper()}"
            )

        super().save(*args, **kwargs)