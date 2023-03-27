from django import forms
from skill_test_app.web.models import *


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
