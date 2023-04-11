from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView


def index(request):
    return render(request, 'index.html')


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'user_register.html'
    context_object_name = 'form'
