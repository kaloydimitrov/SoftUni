from django import forms
from PizzaGang.web.models import Cart, Profile
from django.contrib.auth.models import User


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class UserRegister(forms.ModelForm):
    class Meta:
        model = Profile, User
        fields = ('username', 'first_name', 'last_name', 'profile_picture')
