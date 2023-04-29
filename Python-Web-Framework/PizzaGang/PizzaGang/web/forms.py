from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='')
    first_name = forms.CharField(max_length=30, help_text='')
    last_name = forms.CharField(max_length=30, help_text='')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'first_name': "First Name",
            'last_name': 'Last Name'
        }
