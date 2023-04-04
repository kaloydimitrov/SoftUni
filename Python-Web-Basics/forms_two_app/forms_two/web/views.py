from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person


def home(request):
    return render(request, 'home.html')


def person(request):
    users = Person.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'users.html', context)


def delete_user(request, pk):
    user = Person.objects.get(pk=pk)
    user.delete()

    context = {
        'user': user,
    }

    return render(request, 'deleted_user.html', context)


def index(request):
    if request.method == 'GET':
        form = PersonForm
    else:
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
