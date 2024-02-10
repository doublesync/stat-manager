from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) -> HttpResponse:
    text: str = 'Basketball Stat Manager / Basketball / Home ';
    return HttpResponse(text);