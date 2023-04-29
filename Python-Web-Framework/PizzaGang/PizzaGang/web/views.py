from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from PizzaGang.web.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from PizzaGang.web.models import Pizza


class BaseView(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


#


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'sign-in.html'
    next_page = reverse_lazy('home')


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')


class UserInfoView(TemplateView):
    template_name = 'user-info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ListPizzaView(ListView):
    template_name = 'menu.html'
    model = Pizza


class DetailPizzaView(DetailView):
    template_name = 'pizza-details.html'
    model = Pizza


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


# Testing Authorization and Authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# user = User.objects.create_user('kaloyan', 'kalotablet2006@gmail.com', 'PassMe1234')
user_auth = authenticate(username='kaloyan', password='PassMe1234')

print(user_auth)


def current_user(request):
    user = request.user
    print(user.username)


def logout_example(request):
    print(request.user.__class__.__name__)
    logout(request, user_auth)
    print(request.user.__class__.__name__)
    # TODO: add template
    return render(request, '')
