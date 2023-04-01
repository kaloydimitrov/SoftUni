from django import forms
from black_and_white_app.web.models import User


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
