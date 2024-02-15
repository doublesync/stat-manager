from django.db import models
import basketball.leagueSettings.pDefault as pDefault
import basketball.playerScripts.pCalculate as pCalculate

from copy import deepcopy


# Create your models here
class BasketballPlayer(models.Model):
    first_name: str = models.CharField(max_length=32)
    last_name: str = models.CharField(max_length=32)
    height: int = models.IntegerField()
    weight: int = models.IntegerField()
    wingspan: int = models.IntegerField()
    bmi: float = models.FloatField()
    age: str = models.CharField(max_length=32)
    archetype: str = models.CharField(
        max_length=10,
        choices=[(arch, arch) for arch in pDefault.archetypeChoices],
    )
    position: str = models.CharField(
        max_length=2,
        choices=[(pos, pos) for pos in pDefault.positionChoices],
    )
    secondary_position: str = models.CharField(
        max_length=2,
        choices=[(pos, pos) for pos in pDefault.positionChoices],
    )
    current_team: any = models.OneToOneField(
        "BasketballTeam", on_delete=models.SET_NULL, null=True
    )
    # Copy the defualt attributes
    attributes: any = models.JSONField(default=pDefault.defaultAttributes, blank=True)
    badges: any = models.JSONField(default=pDefault.defaultBadges, blank=True)
    tendencies: any = models.JSONField(default=pDefault.defaultTendencies, blank=True)

    # Other objects
    current_team: any = models.ForeignKey(
        "BasketballTeam", on_delete=models.SET_NULL, null=True
    )

    # What will be displayed in the admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Overriding the save method to calculate some things
    def save(self, *args, **kwargs):
        self.bmi = pCalculate.calculateBMI(self.weight, self.height)
        super().save(*args, **kwargs)


class BasketballTeam(models.Model):
    name: str = models.CharField(max_length=32)
    city: str = models.CharField(max_length=32)
    titles: int = models.IntegerField(default=0)
    players: any = models.ManyToManyField(BasketballPlayer, null=True, blank=True)

    def __str__(self):
        return f"{self.city} {self.name}"
