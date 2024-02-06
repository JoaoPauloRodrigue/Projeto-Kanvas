from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.CoursesView.as_view()),
    path("courses/<pk>/", views.CousersDetailView.as_view()),
    path(
        "courses/<pk>/students/",
        views.CousersDetailStudentView.as_view(),
    ),
    path(
        "courses/<pk>/students/<student_id>/",
        views.CousersDetailStudentView.as_view(),
    ),
]
