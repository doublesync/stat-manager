from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from basketball.forms import BasketballPlayerForm

import basketball.leagueSettings.pDefault as pDefault
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pBadges as pBadges
import basketball.leagueSettings.pPhysical as pPhysical
import basketball.leagueSettings.pLimits as pLimits
import basketball.playerScripts.pCreate as pCreate

from basketball.models import BasketballPlayer

import json


# Create your views here.
@login_required(login_url="/discord/login/")
def home(request) -> render:
    context: dict = {"user": request.user}
    return render(request, "basketball/home.html", context)


@login_required(login_url="/discord/login/")
def create(request) -> render:
    context: dict = {"startingAttributes": pDefault.defaultAttributes()}
    return render(request, "basketball/create.html", context)


def player(request, id: int) -> render:
    context = {
        "player": BasketballPlayer.objects.get(id=id),
        "attributeCategories": pAttributes.attributeCategories,
        "badgeCategories": pBadges.badgeCategories,
    }
    return render(request, "basketball/player.html", context)


# HTMX endpoints
def htmxStartingAttributes(request) -> HttpResponse:
    if request.method == "POST":
        # fmt: off
        height: int = int(request.POST.get("height"))
        archetype: str = request.POST.get("archetype")
        position: str = request.POST.get("position")
        weightModel: str = request.POST.get("weightModel")
        # Validate that height fits within the bounds
        if height > pLimits.playerLimits[archetype][position]["heightLimits"][1]:
            return HttpResponse(f"❌ Height is too tall for {position}.")
        elif height < pLimits.playerLimits[archetype][position]["heightLimits"][0]:   
            return HttpResponse(f"❌ Height is too short for {position}.")
        # Mock player class (so it looks like an object to our functions)
        class MockPlayer:
            def __init__(self):
                self.attributes = pAttributes.startingAttributes[position]
                self.weightModel = weightModel
                self.position = position
                self.archetype = archetype
                self.height = height
        # Create a mock player
        mockPlayer: object = MockPlayer()
        playerReturned: any = pPhysical.setStartingPhysicals(mockPlayer)
        context: dict = {
            "startingAttributes": playerReturned.attributes
        }
        html: str = render_to_string("basketball/htmx/startingAttributes.html", context)
        return HttpResponse(html)


@login_required(login_url="/discord/login/")
def htmxCreate(request) -> HttpResponse:
    if request.method == "POST":
        form = BasketballPlayerForm(request.POST)
        if form.is_valid():
            # Grab the form data
            formData: dict = form.cleaned_data
            # Create the player
            creationAttempt: list = pCreate.createPlayer(request.user, formData)
            player: any = creationAttempt[0]
            response: str = creationAttempt[1]
            if not player:
                # fmt: off
                messages.error(request, response)
                return redirect("basketball:home")
                # fmt: on
            else:
                # Return the HTMX template
                context: dict = {
                    "player": player,
                }
                html: str = render_to_string("basketball/htmx/createHTMX.html", context)
                return HttpResponse(html)
        else:
            messages.error(request, "Player build is not valid - form is not valid.")
            return redirect("basketball:home")
    else:
        messages.error(request, "Player build is not valid - POST request not made.")
        return redirect("basketball:home")
