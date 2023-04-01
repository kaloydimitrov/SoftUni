from django.shortcuts import render, redirect
from black_and_white_app.web.forms import LoginUserForm


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        form = LoginUserForm
    else:
        form = LoginUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)
