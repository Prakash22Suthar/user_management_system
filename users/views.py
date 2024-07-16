from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, RedirectView, DeleteView, ListView, TemplateView, DetailView, View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string


from .forms import UserForm
from .models import CustomUser



class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "user/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["total_user"] = CustomUser.objects.all().count()
        context["active_user_count"] = CustomUser.objects.filter(is_active=True).count()
        context["staff_user_count"] = CustomUser.objects.filter(is_staff=True).count()
        return context

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "user/user_list.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
    
class AddUserView(LoginRequiredMixin, CreateView):
    form_class = UserForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("users:user_list")

class UserDetailsView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "user/user_details.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        context["user_id"] = self.request.user.id
        return context
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("users:user_list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        context["user_id"] =  self.request.GET.get('id', '')
        return context


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "user/confirm_delete.html"
    success_url = reverse_lazy("users:user_list")
    context_object_name = "user"

class AjaxUserListView(LoginRequiredMixin, View): 

    template_name = "user/ajax_user_list.html"   

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all().order_by("-id")
        html = render_to_string(self.template_name, {'users': users})
        return JsonResponse({'html_content': html}, status=200)