from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from courses.models import Enrollment

from .forms import LoginForm, RegisterForm


class RegisterView(CreateView):

    form_class = RegisterForm

    template_name = "accounts/register.html"

    success_url = "/accounts/dashboard/"

    def form_valid(self, form):

        response = super().form_valid(form)

        login(
            self.request,
            self.object
        )

        messages.success(
            self.request,
            "Welcome to Code & Control!"
        )

        return response


class UserLoginView(LoginView):

    authentication_form = LoginForm

    template_name = "accounts/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):

        return "/accounts/dashboard/"


class DashboardView(TemplateView):

    template_name = "accounts/dashboard.html"

    def dispatch(
        self,
        request,
        *args,
        **kwargs
    ):

        if not request.user.is_authenticated:

            return redirect(
                "account_login"
            )

        return super().dispatch(
            request,
            *args,
            **kwargs
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["enrollments"] = Enrollment.objects.filter(
            user=self.request.user
        ).select_related(
            "course"
        )

        return context


class LogoutView(TemplateView):

    template_name = "accounts/logout.html"

    def get(self, request, *args, **kwargs):

        logout(request)

        messages.success(
            request,
            "You have been logged out."
        )

        return redirect("home")