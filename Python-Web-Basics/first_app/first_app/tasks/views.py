from django.shortcuts import render

# Create your views here.
from django import http

from first_app.tasks.models import Task


def show_views(request):
    return http.HttpRequest()


def show_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)
    print(list(all_tasks))
