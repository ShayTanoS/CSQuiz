from django import forms
from .models import Players

class AddPlayerForm(forms.Form):
    number = forms.IntegerField()


class QuizForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Players.objects)