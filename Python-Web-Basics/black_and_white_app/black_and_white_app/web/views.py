from django.http import HttpResponse
from django.shortcuts import render, redirect
from black_and_white_app.web.forms import UserForm


def say_hi(request):
    return HttpResponse('hi')


def login(request):
    if request.method == 'GET':
        form = UserForm
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)
