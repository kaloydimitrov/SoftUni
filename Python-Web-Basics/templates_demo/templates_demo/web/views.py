import random

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Homepage',
        'random_number': random.randint(0, 100)
    }

    return render(request, 'index.html', context)
