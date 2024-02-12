import sys
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

from core.discord import discordAuth
from core.models import DiscordUser

from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def home(request: any) -> render:
    context: dict = {
        'user': request.user
    }
    return render(request, 'core/home.html', context)

def loginDiscord(request: any) -> render:
    discordAuthUrl: str = os.environ.get('DISCORD_AUTH_URL')
    return redirect(discordAuthUrl)

def loginDiscordRedirect(request: any) -> redirect:
    try:
        code: str = request.GET.get('code')
        info: [dict, dict] = discordAuth.exchangeCode(code)
        user: dict = info[0]
        discordUser: any = authenticate(request, user=user) # Not sure of type
        discordUser: any = list(discordUser).pop() # Not sure of type
        login(request, discordUser, 'core.authorize.DiscordBackend')
        messages.success(request, 'You have successfully logged in!')
    except Exception as e:
        messages.error(request, f'There was an error logging in: {e}')
    return redirect('core:home')

def logoutDiscord(request: any) -> redirect:
    logout(request)
    return redirect('core:home')