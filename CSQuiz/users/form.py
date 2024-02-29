from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(), max_length=254)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')