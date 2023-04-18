from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from users_demo.web.models import Pizza, CartItem, Cart
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django import forms


def base(request):
    context = {
        'user': request.user
    }

    return render(request, 'base/base.html', context)


def index(request):
    return render(request, 'index.html')


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class UserRegister(CreateView):
    form_class = MyUserCreationForm
    template_name = 'user_register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class UserLogIn(LoginView):
    template_name = 'user_login.html'
    next_page = reverse_lazy('home')


class UserLogOut(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserDetails(DetailView):
    template_name = 'user_details.html'
    model = User


class ListPizza(ListView):
    template_name = 'menu.html'
    model = Pizza
    context_object_name = 'pizzas'

    def get_queryset(self):
        return Pizza.objects.all().only('name', 'ingredients', 'photo')


class BuyPizza(DetailView):
    template_name = 'pizza_details.html'
    model = Pizza
    context_object_name = 'pizza'


def add_to_cart(request, pizza_id, size):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    item = CartItem.objects.create(pizza=pizza, size=size)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.add(item)
    return redirect('menu')
