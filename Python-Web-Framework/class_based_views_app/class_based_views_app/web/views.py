from django.shortcuts import render
from django.views.generic import TemplateView


def main(request):
    return render(request, 'base.html')


def FBV(request):
    context = {
        'text': "I'm function based view :("
    }

    return render(request, 'index.html', context)


class CBV(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "I'm class based view!"
        return context


class TV(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "I'm template view!"
        return context
