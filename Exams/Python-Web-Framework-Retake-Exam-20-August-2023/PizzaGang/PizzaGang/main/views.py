from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import SignUpForm, UserEditForm, PizzaForm, ProfileEditForm
from .models import Pizza, Profile


def BaseView(request):
    context = {
        'user': request.user
    }

    return render(request, 'base/base.html', context)


class HomeView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'authentication/sign_up.html'
    success_url = reverse_lazy('sign_in')

    # TODO: This fields should be updated in forms.py
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        form.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        return form


class SignInView(LoginView):
    template_name = 'authentication/sign_in.html'
    next_page = reverse_lazy('home')
    form_class = AuthenticationForm

    # TODO: This fields should be updated in forms.py
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['password'].widget.attrs['placeholder'] = 'Password'
        return form


class SignOutView(LogoutView):
    next_page = reverse_lazy('home')


def UserShowView(request, pk):
    user = User.objects.get(pk=pk)

    context = {
        'user': user
    }

    return render(request, 'user_info/show_info.html', context)


def UserEditView(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user_view_link = f'http://127.0.0.1:8000/user-info/show/{pk}/'
            return redirect(user_view_link)
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    }

    return render(request, 'user_info/edit_info.html', context)


def UserAddressView(request, pk):
    pass


class MenuView(ListView):
    template_name = 'pizza/menu.html'
    model = Pizza


def CreatePizzaView(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PizzaForm

    context = {
        'form': form,
    }

    return render(request, 'pizza/create_pizza.html', context)


def EditPizzaView(request, pk):
    pizza = Pizza.objects.get(pk=pk)

    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = PizzaForm(instance=pizza)

    context = {
        'form': form,
        'pizza': pizza
    }

    return render(request, 'pizza/edit_pizza.html', context)


class DeletePizzaView(DeleteView):
    model = Pizza
    template_name = 'pizza/delete_pizza.html'
    success_url = reverse_lazy('menu')