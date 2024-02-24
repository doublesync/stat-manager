from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from basketball.forms import BasketballPlayerForm
from basketball.forms import PlayerUpgradeForm

import basketball.leagueSettings.pDefault as pDefault
import basketball.leagueSettings.pAttributes as pAttributes
import basketball.leagueSettings.pBadges as pBadges
import basketball.leagueSettings.pPhysical as pPhysical
import basketball.leagueSettings.pLimits as pLimits
import basketball.playerScripts.pCreate as pCreate
import basketball.playerScripts.pUpgrade as pUpgrade

from basketball.models import BasketballPlayer
from basketball.models import BasketballTeam
from basketball.models import Voucher
from basketball.models import VoucherReceipt

import core.discord.discordWebhook as discordWebhook

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
    user: any = request.user
    context = {
        "user": user,
        "player": BasketballPlayer.objects.get(id=id),
        "attributeCategories": pAttributes.attributeCategories,
        "badgeCategories": pBadges.badgeCategories,
    }
    return render(request, "basketball/player.html", context)


def playerSearch(request) -> render:
    context: dict = {}
    # Paginate the BasketballPlayer queryset
    playerList: any = BasketballPlayer.objects.all()
    paginator: any = Paginator(playerList, 15)
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


def playerUpgrade(request, id: int) -> render:

    # Check if the user has permission to upgrade the player
    user: any = request.user
    player: any = BasketballPlayer.objects.get(pk=id)
    if not player or player.discordUser != user:
        messages.error(request, "You do not have permission to upgrade this player.")
        return redirect("basketball:home")

    # Send the form to the template
    context: dict = {
        "player": player,
        "form": PlayerUpgradeForm(player=player),
        "attributeCategories": pAttributes.attributeCategories,
        "badgeCategories": pBadges.badgeCategories,
    }
    return render(request, "basketball/playerUpgrade.html", context)


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
    # Check page
    page: int = request.GET.get("page")

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

    # Paginate the page
    paginator: any = Paginator(playerList, 15)
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


def htmxPlayerCart(request, id: int) -> HttpResponse:
    if request.method == "POST":
        # Grab the player
        player: any = BasketballPlayer.objects.get(pk=id)
        # Grab the form data
        form: any = PlayerUpgradeForm(request.POST, player=player)
        context: dict = {
            "player": player,
        }
        if form.is_valid():
            # Grab the form data
            cleanedData: dict = form.cleaned_data
            # Format the data to be used in the upgrade form
            upgradeCart: dict = pUpgrade.compileUpgradeData(player, cleanedData)
            # Return the formatted dictionary in the context
            context["upgradeCart"] = upgradeCart
        else:
            messages.error(request, "Player upgrade is not valid - form is not valid.")
        # Return the HTMX template
        html = render_to_string("basketball/htmx/cartHTMX.html", context)
        return HttpResponse(html)
    else:
        messages.error(request, "Player upgrade is not valid - POST request not made.")
        return redirect("basketball:home")


def sendUpgradeWebhook(player, upgradeAttempt) -> None:
    bodyMessage: str = ""
    if upgradeAttempt["successful"]["attributes"]:
        for details in upgradeAttempt["successful"]["attributes"]:
            bodyMessage += (
                f"✅ **{details[0]}** upgraded from **{details[1]}** to **{details[2]}**.\n"
            )
    if upgradeAttempt["successful"]["badges"]:
        for details in upgradeAttempt["successful"]["badges"]:
            bodyMessage += f"✅ **{details[0]}** upgraded from **{details[1]}** to **{details[2]}**.\n"
    bodyMessage += f"\n[View profile?](https://stat-manager-8e8740f61676.herokuapp.com/basketball/player/{player.id})"
    discordWebhook.send_webhook(
        "upgrade",
        title=f"({ player.id }) {player.firstName} {player.lastName} upgraded for ${upgradeAttempt["cost"]}!",
        message=bodyMessage,
    )
def htmxPlayerUpgrade(request, id: int) -> HttpResponse:
    if request.method == "POST":
        # Grab the player and form validation
        player: any = BasketballPlayer.objects.get(pk=id)
        form: any = PlayerUpgradeForm(request.POST, player=player)
        if form.is_valid():
            # Grab the form data
            cleanedData: dict = form.cleaned_data
            # Validate the upgrade
            upgradeCart: dict = pUpgrade.compileUpgradeData(player, cleanedData)
            upgradeAttempt: list = pUpgrade.purchaseUpgrades(upgradeCart, player)
            print(json.dumps(upgradeAttempt, indent=4))
            # Show errors from "failed" list
            context: dict = {
                "cost": upgradeAttempt["cost"],
                "successful": upgradeAttempt["successful"],
                "failed": upgradeAttempt["failed"],
            }
            # fmt: off
            html: str = render_to_string("basketball/htmx/upgradeResponseHTMX.html", context)
            # fmt: on
            if upgradeAttempt["successful"]["attributes"] or upgradeAttempt["successful"]["badges"]:
                sendUpgradeWebhook(player, upgradeAttempt)
            # Return the HTMX template
            return HttpResponse(html)
        else:
            messages.error(request, "Player upgrade is not valid - form is not valid.")
            return redirect("basketball:home")
