from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import StudentProfile
from courses.models import Enrollment
from .forms import *


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



class StudentProfileView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        profile, created = StudentProfile.objects.get_or_create(
            user=self.request.user
        )

        context["profile"] = profile

        return context
    

class StudentProfileUpdateView(
    LoginRequiredMixin,
    TemplateView
):

    template_name = "accounts/profile_edit.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        profile, created = StudentProfile.objects.get_or_create(
            user=self.request.user
        )

        context["profile"] = profile

        context["user_form"] = UserInformationForm(
            instance=self.request.user
        )

        context["profile_form"] = StudentProfileForm(
            instance=profile
        )

        return context

    def post(self, request, *args, **kwargs):

        profile, created = StudentProfile.objects.get_or_create(
            user=request.user
        )

        user_form = UserInformationForm(
            request.POST,
            instance=request.user
        )

        profile_form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Your profile has been updated successfully."
            )

            return redirect(
                "account_profile"
            )

        context = self.get_context_data()

        context["user_form"] = user_form
        context["profile_form"] = profile_form

        return self.render_to_response(context)
