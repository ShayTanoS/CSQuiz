from django import forms
from .models import Players

class AddPlayerForm(forms.Form):
    number = forms.IntegerField()
