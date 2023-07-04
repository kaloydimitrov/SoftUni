from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, \
    UpdateView, DeleteView
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
    context_object_name = 'tasks'
    ordering = '-category__name'


class TaskDetails(DetailView):
    model = Task
    template_name = 'task-details.html'
    context_object_name = 'task'


# CRUD Views
class TaskCreate(CreateView):
    model = Task
    template_name = 'task-create.html'
    fields = '__all__'
    success_url = reverse_lazy('lv')
    context_object_name = 'form'


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'task-update.html'
    fields = '__all__'
    success_url = reverse_lazy('lv')
    context_object_name = 'form'


class TaskDelete(DeleteView):
    model = Task
    template_name = 'task-delete.html'
    fields = '__all__'
    success_url = reverse_lazy('lv')
    context_object_name = 'form'
