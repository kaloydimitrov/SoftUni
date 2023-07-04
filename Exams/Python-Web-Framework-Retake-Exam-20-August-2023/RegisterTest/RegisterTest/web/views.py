from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm, SignInForm


def HomeView(request):
    context = {
        'user': request.user
    }

    return render(request, 'index.html', context)


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        return render(request, 'sign_up.html', {'form': form})


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'sign_in.html', {'form': form})


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
