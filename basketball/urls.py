from django.urls import path
from django.views.generic import RedirectView

from . import views

# fmt: off
app_name: str = "basketball"
urlpatterns: list = [
    # Combine '' and 'home/' to the same view
    # Redirect '' to 'home/'
    path("", RedirectView.as_view(url="home/")),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("player/<int:id>/", views.player, name="player"),
    path("player/search/", views.playerSearch, name="playerSearch"),
    path("vouchers/", views.vouchers, name="vouchers"),
    path("player/upgrade/<int:id>/", views.playerUpgrade, name="playerUpgrade"),
    # HTMX endpoints
    path("create/htmx/attributes/", views.htmxStartingAttributes, name="htmxStartingAttributes"),
    path("create/htmx/create/", views.htmxCreate, name="htmxCreate"),
    path("player/search/htmx/", views.htmxSearchPlayer, name="htmxSearchPlayer"),
    path("vouchers/htmx/", views.htmxVouchers, name="htmxVouchers"),
]
