from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        error_messages={
            'password_too_similar': '',
            'password_entirely_numeric': '',
        }
    )

    password2 = forms.CharField(
        label="Password Confirmation",
        strip=False,
        widget=forms.PasswordInput,
        error_messages={
            'password_mismatch': '',
        }
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        error_messages={
            'required': '',
            'invalid': ''
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
