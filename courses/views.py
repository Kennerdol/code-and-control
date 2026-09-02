from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from .forms import EnrollmentForm
from .models import Course, Enrollment


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