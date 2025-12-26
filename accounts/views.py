from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy

def in_group(user, name: str) -> bool:
    return user.is_authenticated and user.groups.filter(name=name).exists()

class StudentLoginView(LoginView):
    template_name = "accounts/login_student.html"

    def form_valid(self, form):
        user = form.get_user()
        if not in_group(user, "Students"):
            messages.error(self.request, "Это вход только для студентов.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("student:dashboard")


class TeacherLoginView(LoginView):
    template_name = "accounts/login_teacher.html"

    def form_valid(self, form):
        user = form.get_user()
        if not in_group(user, "Teachers"):
            messages.error(self.request, "Это вход только для преподавателей.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("teacher:dashboard")

