from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from basketball.forms import BasketballPlayerForm

import basketball.leagueSettings.pDefault as pDefault
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pBadges as pBadges
import basketball.leagueSettings.pPhysical as pPhysical
import basketball.leagueSettings.pLimits as pLimits
import basketball.playerScripts.pCreate as pCreate

from basketball.models import BasketballPlayer
from basketball.models import BasketballTeam
from basketball.models import Voucher
from basketball.models import VoucherReceipt

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


def playerSearch(request) -> render:
    context: dict = {}
    # Paginate the BasketballPlayer queryset
    playerList: any = BasketballPlayer.objects.all()
    paginator: any = Paginator(playerList, 10)
    page: int = request.GET.get("page")
    players: any = paginator.get_page(page)
    context["players"] = players
    return render(request, "basketball/playerSearch.html", context)


def vouchers(request) -> render:
    context: dict = {}
    user: any = request.user
    availableVouchers = []
    # Get all vouchers that the user has not redeemed
    for voucher in Voucher.objects.all():
        if not VoucherReceipt.objects.filter(voucher=voucher, discordUser=user):
            availableVouchers.append(voucher)
    # Show all of the available vouchers
    context["availableVouchers"] = availableVouchers
    return render(request, "basketball/vouchers.html", context)


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


def htmxSearchPlayer(request) -> HttpResponse:
    if request.method == "POST":

        # Check searchQuery
        searchQuery: str = request.POST.get("searchQuery")
        if searchQuery:
            playerList: any = BasketballPlayer.objects.filter(
                Q(firstName__icontains=searchQuery) | Q(lastName__icontains=searchQuery)
            )
        else:
            playerList: any = BasketballPlayer.objects.all()

        # Check sortQuery (if it exists)
        sortQuery: str = request.POST.get("sortQuery")
        if sortQuery:
            sortField, sortDirection = sortQuery.split(":")
            playerList = playerList.order_by(
                f"{'-' if sortDirection == 'desc' else ''}{sortField}"
            )

        print(f"Search: {searchQuery}, Sort: {sortQuery}")

        # Paginate the page
        paginator: any = Paginator(playerList, 10)
        page: int = request.GET.get("page")
        players: any = paginator.get_page(page)

        # Return the page
        context: dict = {"players": players}
        html: str = render_to_string("basketball/htmx/searchPlayerTable.html", context)
        return HttpResponse(html)


def htmxVouchers(request) -> HttpResponse:
    if request.method == "POST":
        # Gather the voucher code
        voucherCode: str = request.POST.get("voucherCode")
        discordUser: any = request.user
        # Check if the voucher exists
        voucher: any = Voucher.objects.filter(code=voucherCode).first()
        if not voucher:
            messages.error(request, "Voucher does not exist.")
            return redirect("basketball:vouchers")
        # Check if the user has already redeemed the voucher
        voucherReceipt: any = VoucherReceipt.objects.filter(
            voucher=voucher, discordUser=discordUser
        ).first()
        if voucherReceipt:
            messages.error(request, "You have already redeemed this voucher.")
            return redirect("basketball:vouchers")
        # Redeem the voucher & create a receipt
        discordUserPlayers: any = BasketballPlayer.objects.filter(
            discordUser=discordUser
        )
        for player in discordUserPlayers:
            player.cash += voucher.amount
            player.save()
        VoucherReceipt.objects.create(voucher=voucher, discordUser=discordUser)
        messages.success(request, "Voucher redeemed successfully.")
        html: str = render_to_string("basketball/htmx/voucherHTMX.html")
        # Return with HTMX refresh header
        headers: dict = {"HX-Refresh": "true"}
        return HttpResponse(html, headers=headers)
