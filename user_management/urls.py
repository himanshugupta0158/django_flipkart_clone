from django.urls import path
from .views import LoginView, RegisterView, LogoutView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', RegisterView.as_view(), name="register"),
    path('user_profile', UserProfileView.as_view(), name="user_profile"),
]
