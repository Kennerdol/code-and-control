from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):

    model = Post

    template_name = "blog/post_list.html"

    context_object_name = "posts"

    paginate_by = 9

    def get_queryset(self):

        queryset = (
            Post.objects
            .filter(status="published")
            .order_by("-created_at")
        )

        search_query = self.request.GET.get(
            "q",
            ""
        ).strip()

        category = self.request.GET.get(
            "category",
            ""
        ).strip()

        if search_query:

            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(
                excerpt__icontains=search_query
            ) | queryset.filter(
                content__icontains=search_query
            )

        if category:

            queryset = queryset.filter(
                category=category
            )

        return queryset.distinct()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["search_query"] = self.request.GET.get(
            "q",
            ""
        )

        context["selected_category"] = self.request.GET.get(
            "category",
            ""
        )

        context["categories"] = Post.CATEGORY_CHOICES

        return context


class PostDetailView(DetailView):

    model = Post

    template_name = "blog/post_detail.html"

    context_object_name = "post"

    def get_queryset(self):

        return Post.objects.filter(
            status="published"
        )