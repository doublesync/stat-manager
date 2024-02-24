from django import forms

from basketball.models import BasketballPlayer
from basketball.leagueSettings import pAttributes


class BasketballPlayerForm(forms.ModelForm):
    class Meta:
        model = BasketballPlayer
        fields = [
            "firstName",
            "lastName",
            "weightModel",
            "archetype",
            "position",
            "secondaryPosition",
        ]
        widgets = {
            "firstName": forms.TextInput(attrs={"class": "form-control"}),
            "lastName": forms.TextInput(attrs={"class": "form-control"}),
            "weightModel": forms.Select(attrs={"class": "form-control"}),
            "archetype": forms.Select(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-control"}),
            "secondaryPosition": forms.Select(attrs={"class": "form-control"}),
        }


BADGE_CHOICES = {
    0: "❌ None",
    1: "🟫 Bronze",
    2: "🌫️ Silver",
    3: "🟨 Gold",
    4: "🟪 Hall of Fame",
}


class PlayerUpgradeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        player = kwargs.pop("player", None)
        super().__init__(*args, **kwargs)

        if player:
            # Add form fields dynamically based on the keys and values of the 'attributes' dictionary
            for key, value in player.attributes.items():
                # fmt: off
                if not key in pAttributes.physicalAttributes and not key == "Intangibles":
                    self.fields[f"attributes_{key}"] = forms.IntegerField(
                        label=key,
                        initial=value,
                        widget=forms.NumberInput(attrs={"class": "form-control"}),
                    )
                # fmt: on

            # Add form fields dynamically based on the keys and values of the 'badges' dictionary
            for key, value in player.badges.items():
                # Filter out lower badge levels
                # fmt: off
                filtered_choices = [
                    (value, BADGE_CHOICES[value])
                ]
                for level, label in BADGE_CHOICES.items():
                    if level > value:
                        filtered_choices.append((level, label))
                # fmt: on
                self.fields[f"badges_{key}"] = forms.ChoiceField(
                    label=key,
                    choices=filtered_choices,
                    initial=value,
                    widget=forms.Select(attrs={"class": "form-control"}),
                )
