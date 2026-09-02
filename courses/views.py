from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from courses.services import *

from .forms import *
from .models import *


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(
            status="published"
        )


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

    def get_queryset(self):
        return Course.objects.filter(
            status="published"
        )


class EnrollmentView(FormView):
    template_name = "courses/enroll.html"
    form_class = EnrollmentForm

    def dispatch(self, request, *args, **kwargs):

        self.course = get_object_or_404(
            Course,
            slug=kwargs["slug"],
            status="published"
        )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        kwargs["user"] = self.request.user

        return kwargs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["course"] = self.course

        return context

    def form_valid(self, form):

        enrollment = form.save(commit=False)

        enrollment.course = self.course

        # Associate enrollment with logged-in user
        if self.request.user.is_authenticated:

            enrollment.user = self.request.user

            full_name = self.request.user.get_full_name().strip()

            if not full_name:
                full_name = self.request.user.username

            enrollment.name = full_name
            enrollment.email = self.request.user.email

        enrollment.save()

        messages.success(
            self.request,
            f"You have successfully submitted your enrollment "
            f"request for {self.course.title}."
        )

        return redirect(
            "course_detail",
            slug=self.course.slug
        )


class LessonListView(ListView):

    template_name = "courses/lesson_list.html"

    context_object_name = "lessons"

    def get_queryset(self):

        self.course = get_object_or_404(
            Course,
            slug=self.kwargs["course_slug"],
            status="published"
        )

        return Lesson.objects.filter(
            course=self.course,
            is_published=True
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["course"] = self.course

        context["course_progress"] = 0

        completed_lesson_ids = set()

        if self.request.user.is_authenticated:

            context["course_progress"] = get_course_progress(
                self.request.user,
                self.course
            )

            completed_lesson_ids = set(
                LessonProgress.objects.filter(
                    user=self.request.user,
                    lesson__course=self.course,
                    completed=True
                ).values_list(
                    "lesson_id",
                    flat=True
                )
            )

        context["completed_lesson_ids"] = completed_lesson_ids

        return context
    
class LessonDetailView(DetailView):

    model = Lesson

    template_name = "courses/lesson_detail.html"

    context_object_name = "lesson"

    slug_url_kwarg = "slug"

    def get_queryset(self):

        return Lesson.objects.filter(
            course__slug=self.kwargs["course_slug"],
            course__status="published",
            is_published=True
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        lesson = self.object

        context["course"] = lesson.course

        context["progress"] = None

        if self.request.user.is_authenticated:

            context["progress"] = (
                LessonProgress.objects.filter(
                    user=self.request.user,
                    lesson=lesson
                ).first()
            )

        return context

class LessonCompleteView(
    LoginRequiredMixin,
    DetailView
):

    model = Lesson

    def get_queryset(self):

        return Lesson.objects.filter(
            course__status="published",
            is_published=True
        )

    def get(self, request, *args, **kwargs):

        lesson = self.get_object()

        mark_lesson_complete(
            request.user,
            lesson
        )

        messages.success(
            request,
            f"Lesson '{lesson.title}' marked as complete."
        )

        return redirect(
            "lesson_detail",
            course_slug=lesson.course.slug,
            slug=lesson.slug
        )