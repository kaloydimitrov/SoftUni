from django.shortcuts import render, redirect
from django.http import HttpResponse
from skill_test_app.web.forms import *


def no_users(request):
    users = User.objects.all()
    if len(users) <= 0:
        return True
    return False


def index(request):
    if no_users(request):
        return redirect('create-user')

    context = {
        'login': no_users(request),
        'user': User.objects.get()
    }

    return render(request, 'base.html', context)


def create_user(request):
    if request.method == 'GET':
        form = CreateUser()
    else:
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'users': User.objects.all()
    }

    return render(request, 'login.html', context)


def delete_user(request, pk):
    User.objects.filter(pk=pk).delete()

    return redirect('create-user')


def user_info(request, pk):
    context = {
        'user': User.objects.get(pk=pk)
    }

    return render(request, 'user_info.html', context)
