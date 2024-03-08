from django import forms

class AddPlayerForm(forms.Form):
    number = forms.IntegerField()