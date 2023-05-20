from django import forms
from PizzaGang.web.models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
