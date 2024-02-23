from django import forms
from basketball.models import BasketballPlayer


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

BADGE_CHOICES = [
    ('🟫 Bronze', 1),
    ('🌫️ Silver', 2),
    ('🟨 Gold', 3),
    ('🟪 Hall of Fame', 4),
]

class PlayerUpgradeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        player = kwargs.pop('player', None)
        super().__init__(*args, **kwargs)

        if player:
            # Add form fields dynamically based on the keys and values of the 'attributes' dictionary
            for key, value in player.attributes.items():
                self.fields[f'attributes_{key}'] = forms.IntegerField(
                    label=key, 
                    initial=value,
                    widget=forms.NumberInput(attrs={'class': 'form-control'})
                )

            # Add form fields dynamically based on the keys and values of the 'badges' dictionary
            for key, value in player.badges.items():
                # Filter out lower badge levels
                filtered_choices = [(badge[1], badge[0]) for badge in BADGE_CHOICES if badge[1] >= value]
                
                self.fields[f'badges_{key}'] = forms.ChoiceField(
                    label=key,
                    choices=filtered_choices,
                    initial=value,
                    widget=forms.Select(attrs={'class': 'form-control'})
                )