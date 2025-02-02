from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.register_views, name="sign-up"),
    path("sign-in/", views.login_views, name="sign-in"),
    path("sign-out/", views.logout_views, name="sign-out"),
]
