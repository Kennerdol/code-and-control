from django.utils import timezone

from .models import Lesson, LessonProgress


def mark_lesson_complete(user, lesson):
    """
    Mark a lesson as completed for a specific user.
    """

    progress, created = LessonProgress.objects.get_or_create(
        user=user,
        lesson=lesson,
    )

    progress.completed = True

    if not progress.completed_at:
        progress.completed_at = timezone.now()

    progress.save()

    return progress


def mark_lesson_incomplete(user, lesson):
    """
    Mark a lesson as incomplete.
    """

    progress, created = LessonProgress.objects.get_or_create(
        user=user,
        lesson=lesson,
    )

    progress.completed = False
    progress.completed_at = None

    progress.save()

    return progress


def get_course_progress(user, course):
    """
    Calculate course completion percentage.
    """

    total_lessons = Lesson.objects.filter(
        course=course,
        is_published=True
    ).count()

    if total_lessons == 0:
        return 0

    completed_lessons = LessonProgress.objects.filter(
        user=user,
        lesson__course=course,
        lesson__is_published=True,
        completed=True
    ).count()

    return round(
        (completed_lessons / total_lessons) * 100
    )


def get_course_statistics(user, course):
    """
    Return complete course statistics.
    """

    total_lessons = Lesson.objects.filter(
        course=course,
        is_published=True
    ).count()

    completed_lessons = LessonProgress.objects.filter(
        user=user,
        lesson__course=course,
        lesson__is_published=True,
        completed=True
    ).count()

    progress = 0

    if total_lessons > 0:
        progress = round(
            (completed_lessons / total_lessons) * 100
        )

    status = "Not Started"

    if progress > 0:
        status = "In Progress"

    if progress == 100:
        status = "Completed"

    return {
        "total_lessons": total_lessons,
        "completed_lessons": completed_lessons,
        "progress": progress,
        "status": status,
    }