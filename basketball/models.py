from django.db import models

from core.models import DiscordUser
from core.discord import discordWebhook
import basketball.leagueSettings.pDefault as pDefault
import basketball.playerScripts.pCalculate as pCalculate
import basketball.leagueSettings.pJumpers as pJumpers

from copy import deepcopy


# Create your models here
class BasketballPlayer(models.Model):
    cash: int = models.IntegerField(default=0)
    anomaly: str = models.CharField(max_length=32, default="None")
    firstName: str = models.CharField(max_length=32)
    lastName: str = models.CharField(max_length=32)
    height: int = models.IntegerField()
    formattedHeight: str = models.CharField(max_length=10, default="0'0")
    weight: int = models.IntegerField()
    weightModel: str = models.CharField(
        max_length=10,
        default="Default",
        choices=[(weight, weight) for weight in pDefault.weightChoices],
    )
    wingspan: int = models.IntegerField()
    bmi: float = models.FloatField()
    archetype: str = models.CharField(
        max_length=10,
        choices=[(arch, arch) for arch in pDefault.archetypeChoices],
    )
    position: str = models.CharField(
        max_length=2,
        choices=[(pos, pos) for pos in pDefault.positionChoices],
    )
    secondaryPosition: str = models.CharField(
        max_length=2,
        choices=[(pos, pos) for pos in pDefault.positionChoices],
    )
    attributes: any = models.JSONField(default=pDefault.defaultAttributes, blank=True)
    badges: any = models.JSONField(default=pDefault.defaultBadges, blank=True)
    tendencies: any = models.JSONField(default=pDefault.defaultTendencies, blank=True)
    jumpshot: str = models.CharField(default="None", max_length=32, blank=True)

    # Foreign keys
    discordUser: any = models.ForeignKey(
        "core.DiscordUser",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="players",
    )
    currentTeam: any = models.ForeignKey(
        "BasketballTeam", on_delete=models.SET_NULL, blank=True, null=True
    )

    # What will be displayed in the admin panel
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    # Overriding the save method to calculate some things
    def save(self, *args, **kwargs):
        # Calculate the BMI and formatted height
        self.bmi = pCalculate.calculateBMI(self.weight, self.height)
        self.formattedHeight = pCalculate.formatHeight(self.height)
        # Calculate the lateral quickness
        self.attributes["Lateral Quickness"] = (
            self.attributes["Speed"] + self.attributes["Perimeter Defense"]
        ) // 2
        # Calculate the jumpshot (only skilled players choose their jumpshot)
        if self.jumpshot == "None" and self.archetype != "Skilled":
            self.jumpshot = pJumpers.rollJumper(self.height)
            # fmt: off
            print(f"{self.firstName} {self.lastName} has a new jumpshot: {self.jumpshot}")
            # fmt: on
        # Save the model
        super().save(*args, **kwargs)


class BasketballTeam(models.Model):
    name: str = models.CharField(max_length=32)
    city: str = models.CharField(max_length=32)
    titles: int = models.IntegerField(default=0)
    players: any = models.ManyToManyField(BasketballPlayer, null=True, blank=True)

    def __str__(self):
        return f"{self.city} {self.name}"


class Voucher(models.Model):
    code: str = models.CharField(max_length=32)
    amount: int = models.IntegerField()
    active: bool = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.amount}"


class VoucherReceipt(models.Model):
    discordUser: any = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    voucher: any = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    date: any = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.discordUser.discord_tag} used {self.voucher.code}"


class UpgradeReceipt(models.Model):
    discordUser: any = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    player: any = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE)
    successful: any = models.JSONField()
    failed: any = models.JSONField()
    date: any = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.discordUser.discord_tag} upgraded {self.player.firstName} {self.player.lastName}"

    def save(self, *args, **kwargs):
        # Create the message
        bodyMessage: str = ""
        totalCost: int = 0
        for details in self.successful["attributes"]:
            bodyMessage += f"✅ **{details[0]}** upgraded from **{details[1]}** to **{details[2]}**.\n"
        for details in self.successful["badges"]:
            bodyMessage += f"✅ **{details[0]}** upgraded from **{details[1]}** to **{details[2]}**.\n"
        bodyMessage += f"\n[View profile?](https://stat-manager-8e8740f61676.herokuapp.com/basketball/player/{self.player.id})"
        # Send the webhook
        discordWebhook.send_webhook(
            "upgrade",
            title=f"({self.player.id}) {self.player.firstName} {self.player.lastName} upgraded for ${totalCost}!",
            message=bodyMessage,
        )
        # Save the model
        super().save(*args, **kwargs)


class CashReceipt(models.Model):
    discordUser: any = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    player: any = models.ForeignKey(BasketballPlayer, on_delete=models.CASCADE)
    amount: int = models.IntegerField()
    taken: bool = models.BooleanField(default=False)
    payReason: str = models.CharField(max_length=30, default="None")
    jobType: str = models.CharField(max_length=10, default="Misc")
    date: any = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.discordUser.discord_tag} gave {self.player.firstName} {self.player.lastName} {self.amount} cash"

    def save(self, *args, **kwargs):
        # Create the message
        bodyMessage: str = (
            f"💵 **{self.amount}** cash {'taken' if self.taken else 'given'}: **{self.player.firstName} {self.player.lastName}**.\n```Job Type: {self.jobType}```\n```Reason: {self.payReason}```"
        )
        bodyMessage += f"\n[View profile?](https://stat-manager-8e8740f61676.herokuapp.com/basketball/player/{self.player.id})"
        # Send the webhook
        discordWebhook.send_webhook(
            "cash",
            title=f"({self.player.id}) {self.player.firstName} {self.player.lastName} {'lost' if self.taken else 'gained'} ${self.amount}!",
            message=bodyMessage,
        )
        # Save the model
        super().save(*args, **kwargs)
