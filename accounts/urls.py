from django.urls import path

from .views import (
    DashboardView,
    LogoutView,
    RegisterView,
    UserLoginView,
)


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

]