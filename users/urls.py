from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import about, homepage, profile, registration

urlpatterns = [
    path("", homepage, name="homepage"),
    path("about/", about, name="about"),
    path("profile/", profile, name="profile"),
    path("register", registration, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]
