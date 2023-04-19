from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class BaseView(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'Hello, World!'
        return context


class HomeView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    form_class = User
    template_name = 'register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


# Rewriting UserCreationForm
class SignInUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignIn(LoginView):
    form_class = UserCreationForm
    template_name = 'register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class SignOut(LogoutView)
