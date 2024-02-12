from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name: str = 'core'
urlpatterns: list = [
    path("", RedirectView.as_view(url="/home/")),
    path("home/", views.home, name="home"),
    path("discord/login/", views.loginDiscord, name="loginDiscord"),
    path("discord/login/redirect/", views.loginDiscordRedirect, name="loginDiscordRedirect"),
    path("discord/logout/", views.logoutDiscord, name="logoutDiscord"),
]