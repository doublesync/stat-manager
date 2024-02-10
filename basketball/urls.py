from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name: str = 'basketball';
urlpatterns: list = [
    # Combine '' and 'home/' to the same view
    # Redirect '' to 'home/'
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.home, name='home'),
]