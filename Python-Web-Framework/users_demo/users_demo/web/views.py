from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView


def base(request):
    context = {
        'user': request.user
    }

    return render(request, 'base/base.html', context)


def index(request):
    return render(request, 'index.html')


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'user_register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class UserLogin(LoginView):
    template_name = 'user_login.html'
    success_url = reverse_lazy('home')


class UserDetails(DetailView):
    template_name = 'user_details.html'
    model = User
