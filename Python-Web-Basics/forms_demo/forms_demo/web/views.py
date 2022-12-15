from django.http import HttpResponse
from django import forms
from django.shortcuts import render


def home(request):
    return HttpResponse('This is home!')


class FirstForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField(required=True)


def index(request):
    if request.method == "GET":
        form = FirstForm
    else:
        form = FirstForm(request.POST)

    context = {
        "form": FirstForm,
    }

    return render(request, 'index.html', context)
