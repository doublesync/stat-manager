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
