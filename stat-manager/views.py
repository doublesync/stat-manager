from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def home(request) -> HttpResponse:
    return redirect('core:home')