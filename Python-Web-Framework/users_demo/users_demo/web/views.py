from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from users_demo.web.models import Pizza
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
