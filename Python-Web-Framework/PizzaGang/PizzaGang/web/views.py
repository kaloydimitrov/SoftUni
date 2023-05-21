from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from PizzaGang.web.models import Pizza, Cart
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BaseView(ListView):
    template_name = 'base/base.html'
    model = Cart
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzas'] = Pizza.objects.all()
        return context


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'sign-in.html'
    next_page = reverse_lazy('home')


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')

class ListPizzaView(ListView):
    template_name = 'menu.html'
    model = Pizza


class DetailPizzaView(DetailView):
    template_name = 'pizza-details.html'
    model = Pizza


@login_required
def add_to_cart(request, pizza_pk):
    pizza = get_object_or_404(Pizza, pk=pizza_pk)

    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))

        cart = Cart(pizza=pizza, size=size, quantity=quantity)
        cart.save()

        return redirect('menu')

    return render(request, 'pizza-details.html', )


class UserInfoBase(DetailView):
    template_name = 'user-info-base.html'
    model = User


class UserInfoDetails(DetailView):
    template_name = 'user-info-details.html'
    model = User


class UserInfoAddress(DetailView):
    template_name = 'user-info-address.html'
    model = User


class UserInfoOrders(DetailView):
    template_name = 'user-info-orders.html'
    model = User


class UserInfoHistory(DetailView):
    template_name = 'user-info-history.html'
    model = User


def handler404(request, exception=None):
    return render(request, '404.html', status=404)
