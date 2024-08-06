from django import forms

from my_app.models import games


class gamesForm(forms.ModelForm):
    class Meta:
        model = games
        fields = ("__all__")