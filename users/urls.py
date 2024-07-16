from django.urls import path, include
from .views import UserDashboardView, UserListView, AddUserView, UserDetailsView, DeleteUserView, UserUpdateView, AjaxUserListView

app_name = "users"

urlpatterns = [
    path("", UserDashboardView.as_view(), name="dashboard"),
    path('user-list', UserListView.as_view(), name="user_list"),
    path('user-add', AddUserView.as_view(), name="add_user"),
    path('user-detail/<int:pk>', UserDetailsView.as_view(), name="user_details"),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name="update_user"),
    path('user-delete/<int:pk>', DeleteUserView.as_view(), name="delete_user"),
    # path("", UserListView.as_view(), name = "user_list"),

    path('ajax-user-list', AjaxUserListView.as_view(), name="ajax_user_list"),
]