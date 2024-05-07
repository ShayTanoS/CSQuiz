from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(), max_length=254)
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}))
    password2 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class EmailConfirmForm(forms.Form):
    code = forms.IntegerField()
