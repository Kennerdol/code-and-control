from django.urls import include, path
from .views import *


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("projects/", include("portfolio.urls")),
    path("skills/", SkillsView.as_view(), name="skills"),
    path("blogs/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path("courses/", include("courses.urls")),
    path("resources/", include("resources.urls")),
    path("newsletter/", include("newsletter.urls")),

]