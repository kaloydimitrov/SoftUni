from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from class_based_views_app.web.models import Category, Task


def main(request):
    return render(request, 'base/base.html')


def FBV(request):
    context = {
        'text': "I'm function based view :("
    }

    return render(request, 'index.html', context)


class CBV(View):
    def get(self, request, *args, **kwargs):
        context = {
            'text': "I'm class based view!"
        }

        return render(request, 'index.html', context)


class TV(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'text': "I'm template view!"
        }


# Generic Views

class TaskList(ListView):
    model = Task
    template_name = 'task-list.html'
    ordering = '-category__name'
    context_object_name = 'tasks'


class TaskDetails(DetailView):
    model = Task
    template_name = 'task-details.html'
    context_object_name = 'task'
