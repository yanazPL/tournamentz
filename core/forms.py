from django import forms
from core.models import Tournament

class CreateTournamentForm(forms.Form):
    name = forms.CharField(max_length=200)
    # brackest_type = forms.charField(
    #     max_length = 2,
    #     choices = Tournament.BRACKET_TYPE_CHOICES,
    #     default = Tournament.SINGLE_ELIMINATION,
    # )
    bracket_type = forms.ChoiceField(
        choices = Tournament.BRACKET_TYPE_CHOICES
    )
    player_list = forms.CharField(max_length=16384, widget=forms.Textarea)

