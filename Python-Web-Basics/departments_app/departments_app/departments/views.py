from django.http import HttpResponse
from django.shortcuts import render


def new_view(request):
    return HttpResponse('first HttpResponse')


def text(request):
    index = {
        'say_hi': 'hi',
        'dapartments': {
            'dep1',
            'dep2',
            'dep3'
            }
    }

    return render(request, 'index.html', context=None)
