from django.urls import include, path, reverse_lazy
from users.views import *
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    #path("accounts/password-change/", auth_views.PasswordChangeView.as_view(template_name="registration/password-change.html"), name="password-change"),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path("accounts/password_change/", auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("users:password_change_done")),name='password_change'),
    path('', dashboard, name="dashboard")
]