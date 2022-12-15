from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from forms_demo.web.models import Person


def home(request):
    return HttpResponse('This is home!')


class FirstForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField(required=True)


def index(request):
    name = None
    if request.method == "GET":
        form = FirstForm
    else:
        form = FirstForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name,
        )

    context = {
        "form": FirstForm,
        "name": name,
    }

    return render(request, 'index.html', context)
