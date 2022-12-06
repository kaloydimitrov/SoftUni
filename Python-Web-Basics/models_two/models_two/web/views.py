from django.http import HttpResponse
from django.shortcuts import render
from models_two.web.models import Employees


def home(request):
    return HttpResponse('This is home!')


def employee_details(request):
    context = {
        "employees": Employees.objects.all(),
    }

    return render(request, 'index.html', context)
