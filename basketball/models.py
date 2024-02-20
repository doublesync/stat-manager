from django.db import models
import basketball.leagueSettings.pDefault as pDefault
import basketball.playerScripts.pCalculate as pCalculate

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
        self.bmi = pCalculate.calculateBMI(self.weight, self.height)
        self.formattedHeight = pCalculate.formatHeight(self.height)
        self.attributes["Lateral Quickness"] = (self.attributes["Speed"] + self.attributes["Perimeter Defense"]) // 2 
        super().save(*args, **kwargs)


class BasketballTeam(models.Model):
    name: str = models.CharField(max_length=32)
    city: str = models.CharField(max_length=32)
    titles: int = models.IntegerField(default=0)
    players: any = models.ManyToManyField(BasketballPlayer, null=True, blank=True)

    def __str__(self):
        return f"{self.city} {self.name}"
