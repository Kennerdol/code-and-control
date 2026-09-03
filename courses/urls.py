from django.urls import path

from .views import (
    CertificateDetailView,
    CourseDetailView,
    CourseListView,
    EnrollmentView,
    LessonCompleteView,
    LessonDetailView,
    LessonListView,
)


urlpatterns = [

    path("", CourseListView.as_view(), name="course_list"),
    path("<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("<slug:slug>/enroll/", EnrollmentView.as_view(), name="course_enroll"),
    path("<slug:course_slug>/lessons/", LessonListView.as_view(), name="lesson_list"),
    path("<slug:course_slug>/lessons/<slug:slug>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("<slug:course_slug>/lessons/<slug:slug>/complete/", LessonCompleteView.as_view(), name="lesson_complete"),
    # path("certificates/<uuid:certificate_id>/", CertificateDetailView.as_view(), name="certificate_detail"),
    path("certificates/<int:certificate_id>/", CertificateDetailView.as_view(), name="certificate_detail"),
]