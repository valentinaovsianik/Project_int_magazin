from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
