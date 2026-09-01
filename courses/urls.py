from django.urls import path

from .views import (
    CourseDetailView,
    CourseListView,
    EnrollmentView,
)


urlpatterns = [

    path("", CourseListView.as_view(), name="course_list"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("<slug:slug>/enroll/", EnrollmentView.as_view(), name="course_enroll"),

]