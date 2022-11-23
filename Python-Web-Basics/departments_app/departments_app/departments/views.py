from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('This is home')


def department(request):
    return HttpResponse('This is the default department')


def department_details(request, department_id):
    return HttpResponse(f'This is department {department_id}')
