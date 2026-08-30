from django.views.generic import ListView, DetailView

from .models import Resource


class ResourceListView(ListView):

    model = Resource

    template_name = "resources/resource_list.html"

    context_object_name = "resources"

    paginate_by = 12

    def get_queryset(self):

        return (
            Resource.objects
            .filter(status="published")
            .order_by("-created_at")
        )


class ResourceDetailView(DetailView):

    model = Resource

    template_name = "resources/resource_detail.html"

    context_object_name = "resource"

    def get_queryset(self):

        return Resource.objects.filter(
            status="published"
        )