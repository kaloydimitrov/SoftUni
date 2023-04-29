from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from PizzaGang.web.models import Pizza


@login_required
def add_to_cart(request, pk):
    pizza = Pizza.objects.get(id=pk)
    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        cart_item = CartItem.objects.create(pizza=pizza, size=size, quantity=quantity)
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart.items.add(cart_item)
        return redirect('cart')
    return render(request, 'add_to_cart.html', {'pizza': pizza})
