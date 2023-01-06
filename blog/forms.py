from django import forms


class GameForm(forms.Form):
    damage = forms.IntegerField()
