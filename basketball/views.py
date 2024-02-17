from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from basketball.forms import BasketballPlayerForm

import basketball.leagueSettings.pDefault as pDefault
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pPhysical as pPhysical
import basketball.leagueSettings.pLimits as pLimits


# Create your views here.
def home(request) -> render:
    return render(request, "basketball/home.html")


def create(request) -> render:
    context = {"startingAttributes": pDefault.defaultAttributes()}
    return render(request, "basketball/create.html", context)


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
