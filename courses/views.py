from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from .forms import EnrollmentForm
from .models import Course


class CourseListView(ListView):

    model = Course

    template_name = "courses/course_list.html"

    context_object_name = "courses"

    def get_queryset(self):

        return Course.objects.filter(
            status="published"
        ).order_by("-created_at")


class CourseDetailView(DetailView):

    model = Course

    template_name = "courses/course_detail.html"

    context_object_name = "course"

    def get_queryset(self):

        return Course.objects.filter(
            status="published"
        )


class EnrollmentView(FormView):

    form_class = EnrollmentForm

    template_name = "courses/enroll.html"

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

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["course"] = self.course

        return context


    def form_valid(self, form):

        enrollment = form.save(
            commit=False
        )

        enrollment.course = self.course

        if self.request.user.is_authenticated:

            enrollment.user = self.request.user

            enrollment.name = (
                self.request.user.get_full_name()
                or self.request.user.username
            )

            enrollment.email = (
                self.request.user.email
            )

        enrollment.save()

        messages.success(
            self.request,
            (
                "Your enrollment request has been received. "
                "We'll contact you shortly."
            )
        )

        return redirect(
            "course_detail",
            slug=self.course.slug
        )


    def form_invalid(self, form):

        messages.error(
            self.request,
            "Please correct the errors below."
        )

        return super().form_invalid(form)