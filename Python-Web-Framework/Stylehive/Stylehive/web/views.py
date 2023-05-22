from django.shortcuts import render

from django.views.generic import TemplateView


def BaseView(request):
    context = {
        'user': request.user
    }

    return render(request, 'base', context)


class IndexView(TemplateView):
    template_name = 'index.html'
