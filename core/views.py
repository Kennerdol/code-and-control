from django.views.generic import TemplateView

from portfolio.models import Project


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_projects"] = (
            Project.objects
            .filter(featured=True)
            .order_by("-created_at")[:3]
        )

        return context


class AboutView(TemplateView):
    template_name = "about.html"