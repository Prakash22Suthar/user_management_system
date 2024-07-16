from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


from .forms import CustomLoginForm, UserSignUpForm


# Create your views here.


class LoginPageView(LoginView):
    template_name = "base/index.html"
    form_class = CustomLoginForm
    # success_url = reverse_lazy("users:dashboard")

    def get_success_url(self):
        return reverse_lazy("users:dashboard")

class UserSignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = "user/signup.html"
    success_url = reverse_lazy("base:login")