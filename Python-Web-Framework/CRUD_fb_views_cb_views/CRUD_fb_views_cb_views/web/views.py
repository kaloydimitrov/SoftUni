from django.shortcuts import render, redirect
from django.views import View

from CRUD_fb_views_cb_views.web.models import Task
from CRUD_fb_views_cb_views.web.forms import TaskForm


def HomeView(request):
    if request.method == 'POST':
        task_name = request.POST.get('name')
        Task.objects.create(name=task_name)

        task_desc = request.POST.get('desc')
        Task.objects.create(description=task_desc)

        return redirect('home')

    context = {
        'tasks': Task.objects.all(),
    }

    return render(request, 'index.html', context)


def TaskUpdate(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskForm(instance=Task)

    context = {
        'form': form,
    }

    return render(request, 'tast-update.html', context)
