from django.urls import path
from .views import LoginPageView, UserSignUpView
from django.contrib.auth.views import LogoutView

app_name="base"


urlpatterns = [
    path('', LoginPageView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("signup", UserSignUpView.as_view(), name="signup"),
    
]