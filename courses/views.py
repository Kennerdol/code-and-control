from django.views.generic import ListView, DetailView

from .models import Course


class CourseListView(ListView):

    model = Course

    template_name = "courses/course_list.html"

    context_object_name = "courses"

    queryset = Course.objects.filter(
        published=True
    )


class CourseDetailView(DetailView):

    model = Course

    template_name = "courses/course_detail.html"

    context_object_name = "course"

    slug_field = "slug"

    slug_url_kwarg = "slug"