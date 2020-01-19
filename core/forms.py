"""Module contains form allowing for tournament creation"""

from django import forms
from core.models import Tournament


class CreateTournamentForm(forms.Form):
    """Simple form for quick tournament creation"""
    name = forms.CharField(max_length=200)
    bracket_type = forms.ChoiceField(
        choices=Tournament.BRACKET_TYPE_CHOICES,
    )
    player_list = forms.CharField(max_length=16384, widget=forms.Textarea)
