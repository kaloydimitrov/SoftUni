from django.shortcuts import render, redirect
from forms_demo.web.forms import FirstForm


def home(request):
    return render(request, 'home_page.html')


def forms(request):
    if request.method == 'GET':
        form = FirstForm
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            pass
            return redirect('http://127.0.0.1:8000/')

    context = {
        'form': FirstForm,
    }

    return render(request, 'forms.html', context)
