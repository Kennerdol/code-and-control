from django.conf.urls import static
from django.urls import path

from config import settings

from .views import *


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="account_register",
    ),

    path(
        "login/",
        UserLoginView.as_view(),
        name="account_login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="account_logout",
    ),

    path(
        "dashboard/",
        DashboardView.as_view(),
        name="account_dashboard",
    ),

    path(
        "profile/",
        StudentProfileView.as_view(),
        name="account_profile"
    ),

    path(
        "profile/edit/",
        StudentProfileUpdateView.as_view(),
        name="account_profile_edit"
    ),

]