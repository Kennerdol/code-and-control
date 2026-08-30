from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogListView(ListView):

    model = BlogPost

    template_name = "blog/blog_list.html"

    context_object_name = "posts"

    paginate_by = 6

    def get_queryset(self):
        return (
            BlogPost.objects
            .filter(published=True)
            .select_related("category")
        )


class BlogDetailView(DetailView):

    model = BlogPost

    template_name = "blog/blog_detail.html"

    context_object_name = "post"

    slug_field = "slug"

    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            BlogPost.objects
            .filter(published=True)
            .select_related("category")
        )