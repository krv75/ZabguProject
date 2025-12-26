from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import StudentLoginView, TeacherLoginView

urlpatterns = [
    path("login/student/", StudentLoginView.as_view(), name="login_student"),
    path("login/teacher/", TeacherLoginView.as_view(), name="login_teacher"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
